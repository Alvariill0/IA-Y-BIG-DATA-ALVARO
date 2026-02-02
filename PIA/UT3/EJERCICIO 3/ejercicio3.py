# EJERCICIO 3 - Entrega Parcial 1 - ALVARO FERNANDEZ BECERRA
# Módulo para comunicación con la base de datos.
# Debe incluir:
# o Insertar datos de países, fronteras y temperaturas
# o Recuperar datos de países, temperaturas, fronteras y temperaturas de las fronteras.

import mysql.connector
import json
import os
from datetime import datetime

# CONFIGURACIÓN DE LA BASE DE DATOS
CONFIG_DB = {
    'host': 'localhost',
    'user': 'root',
    'password': 'alvaro',
    'database': 'temperaturas'
}
API_KEY = "fa905b4ca52cfdbb2ed4d595dd07d816"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
def conectar_bd():
    """
    Crea y devuelve una conexión a la base de datos.
    """
    conexion = mysql.connector.connect(**CONFIG_DB)
    return conexion

def insertar_pais(conexion, cca2, cca3, nombre, capital, region, subregion, miembro_ue, latitud=None, longitud=None):
    """
    Inserta un país en la base de datos.
    """
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO paises (cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (cca2, cca3, nombre, capital, region, subregion, miembro_ue, latitud, longitud)
    cursor.execute(consulta, valores)
    conexion.commit()
    id_pais = cursor.lastrowid
    cursor.close()
    return id_pais

def insertar_frontera(conexion, id_pais, cca3_frontera):
    """
    Inserta una frontera para un país.
    """
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO fronteras (idpais, cca3_frontera)
        VALUES (%s, %s)
    """
    valores = (id_pais, cca3_frontera)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()

def insertar_temperatura(conexion, id_pais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer):
    """
    Inserta un registro de temperatura para un país.
    """
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO temperaturas (idpais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (id_pais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()

def obtener_todos_paises(conexion):
    """
    Obtiene todos los países de la base de datos.
    """
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT idpais, cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud
        FROM paises
        ORDER BY nombre
    """
    cursor.execute(consulta)
    paises = cursor.fetchall()
    cursor.close()
    return paises

def obtener_temperaturas(conexion):
    """
    Recupera datos de temperaturas con nombre del país.
    """
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT t.*, p.nombre, p.cca3
        FROM temperaturas t
        JOIN paises p ON t.idpais = p.idpais
        ORDER BY t.timestamp DESC
    """
    cursor.execute(consulta)
    temperaturas = cursor.fetchall()
    cursor.close()
    return temperaturas

def obtener_fronteras(conexion):
    """
    Recupera datos de fronteras con nombres de países.
    """
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT f.*, p.nombre AS pais_nombre, pf.nombre AS frontera_nombre
        FROM fronteras f
        JOIN paises p ON f.idpais = p.idpais
        LEFT JOIN paises pf ON f.cca3_frontera = pf.cca3
        ORDER BY p.nombre
    """
    cursor.execute(consulta)
    fronteras = cursor.fetchall()
    cursor.close()
    return fronteras

def obtener_temperaturas_fronteras(conexion, nombre_pais):
    """
    Obtiene temperaturas de un país y sus países fronterizos.
    """
    cursor = conexion.cursor(dictionary=True)
    
    # Buscar el país
    cursor.execute("SELECT idpais FROM paises WHERE nombre = %s", (nombre_pais,))
    pais_result = cursor.fetchone()
    if not pais_result:
        cursor.close()
        return None
    id_pais = pais_result['idpais']
    
    # Temperatura del país
    cursor.execute("""
        SELECT t.* FROM temperaturas t
        WHERE t.idpais = %s
        ORDER BY t.timestamp DESC LIMIT 1
    """, (id_pais,))
    temp_pais = cursor.fetchone()
    
    # Fronteras con temperaturas
    cursor.execute("""
        SELECT DISTINCT pf.nombre AS frontera_nombre, pf.cca3, t.*
        FROM fronteras f
            JOIN paises pf ON f.cca3_frontera = pf.cca3
        JOIN temperaturas t ON pf.idpais = t.idpais
        WHERE f.idpais = %s
        ORDER BY pf.nombre, t.timestamp DESC
    """, (id_pais,))
    temps_fronteras = cursor.fetchall()
    
    cursor.close()
    return {
        'pais': nombre_pais,
        'temp_pais': temp_pais,
        'temps_fronteras': temps_fronteras
    }

def insertar_desde_json(conexion, ruta_json):
    """
    Inserta datos de países y fronteras desde JSON.
    """
    # Manejar rutas absolutas / relativas
    ruta = ruta_json if os.path.isabs(ruta_json) else os.path.join(os.path.dirname(__file__), ruta_json)
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra el archivo JSON: {ruta}")

    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    for pais_data in datos:
        cca2 = pais_data['cca2']
        cca3 = pais_data['cca3']
        nombre = pais_data['name']['common']
        capital = pais_data.get('capital', [''])[0] if pais_data.get('capital') else ''
        region = pais_data['region']
        subregion = pais_data.get('subregion', '')
        latlng = pais_data.get('latlng', [None, None])
        latitud, longitud = latlng[0], latlng[1]
        miembro_ue = 1 if any(c in cca3 for c in ['ESP', 'FRA', 'DEU', 'ITA', 'BEL', 'NLD', 'LUX', 'AUT', 'PRT']) else 0
        
        id_pais = insertar_pais(conexion, cca2, cca3, nombre, capital, region, subregion, miembro_ue, latitud, longitud)
        
        borders = pais_data.get('borders', [])
        for cca3_frontera in borders:
            insertar_frontera(conexion, id_pais, cca3_frontera)


def prueba():
    print("=== PRUEBA MÓDULO BD ===")
    conexion = conectar_bd()
    
    # Insertar desde JSON (países y fronteras)
    print("1 INERTAR PAISES")
    insertar_desde_json(conexion, "PaisesEjemplo.json")
    
    # Recuperar datos
    print("\n 2 MOSTRAR INSERCIONES:")
    paises = obtener_todos_paises(conexion)
    print(f"Total: {len(paises)} países")
    
    print("\n3 ") # falta implementar api
    temps = obtener_temperaturas(conexion)
    print(f"Total: {len(temps)} registros")
    
    print("\n4. Fronteras:")
    frs = obtener_fronteras(conexion)
    print(f"Total: {len(frs)} fronteras")
    # Mostrar una frontera:
    for fr in frs:
        if fr['pais_nombre'] == 'Estonia':
            print(fr)
            break
    
    print("\n5. Temps. España y fronteras:")
    res = obtener_temperaturas_fronteras(conexion, "Spain")
    print(res)

    print("--------------.")
    conexion.close()
    

def limpiar_bd():
    """
    Limpia las tablas de la base de datos.
    """
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM temperaturas")
    cursor.execute("DELETE FROM fronteras")
    cursor.execute("DELETE FROM paises")
    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    prueba()
    # limpiar_bd()
