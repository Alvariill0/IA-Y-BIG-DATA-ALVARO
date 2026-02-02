"""

EJERCICIO 3 -Entrega Parcial 1 - ÁLVARO FERNANDEZ BECERRA

Módulo para comunicación con la base de datos. Debe incluir:

o   Insertar datos de países, fronteras y temperaturas

o   Recuperar datos de países, temperaturas, fronteras y temperaturas de las fronteras.
"""

import mysql.connector
from datetime import datetime


#  CONFIGURACIÓN 

CONFIG_DB = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Pon aquí tu contraseña
    'database': 'temperaturas'
}


#  CONEXIÓN 

def conectar_bd():
    """
    Crea y devuelve una conexión a la base de datos
    """
    conexion = mysql.connector.connect(
        host=CONFIG_DB['host'],
        user=CONFIG_DB['user'],
        password=CONFIG_DB['password'],
        database=CONFIG_DB['database']
    )
    return conexion


# ==================== INSERCIÓN DE DATOS ====================

def insertar_pais(conexion, cca2, cca3, nombre, capital, region, subregion, miembro_ue, latitud=None, longitud=None):
    """
    Inserta un país en la base de datos
    
    Parámetros:
        conexion: conexión a la base de datos
        cca2: código de 2 letras del país
        cca3: código de 3 letras del país
        nombre: nombre del país
        capital: capital del país
        region: región geográfica
        subregion: subregión geográfica
        miembro_ue: True si es miembro de la UE, False si no
        latitud: latitud de la capital (opcional)
        longitud: longitud de la capital (opcional)
    
    Devuelve:
        El ID del país insertado
    """
    cursor = conexion.cursor()
    
    consulta = """
        INSERT INTO paises 
        (cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    valores = (cca2, cca3, nombre, capital, region, subregion, miembro_ue, latitud, longitud)
    
    cursor.execute(consulta, valores)
    conexion.commit()
    
    id_pais = cursor.lastrowid
    
    cursor.close()
    
    return id_pais


def insertar_frontera(conexion, idpais, cca3_frontera):
    """
    Inserta una frontera para un país
    
    Parámetros:
        conexion: conexión a la base de datos
        idpais: ID del país
        cca3_frontera: código cca3 del país fronterizo
    """
    cursor = conexion.cursor()
    
    consulta = "INSERT INTO fronteras (idpais, cca3_frontera) VALUES (%s, %s)"
    valores = (idpais, cca3_frontera)
    
    cursor.execute(consulta, valores)
    conexion.commit()
    
    cursor.close()


def insertar_temperatura(conexion, idpais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer):
    """
    Inserta un registro de temperatura para un país
    
    Parámetros:
        conexion: conexión a la base de datos
        idpais: ID del país
        timestamp: fecha y hora del registro (datetime)
        temperatura: temperatura actual
        sensacion: sensación térmica
        minima: temperatura mínima
        maxima: temperatura máxima
        humedad: porcentaje de humedad
        amanecer: hora de amanecer (formato "HH:MM:SS")
        atardecer: hora de atardecer (formato "HH:MM:SS")
    
    Devuelve:
        El ID del registro de temperatura insertado
    """
    cursor = conexion.cursor()
    
    consulta = """
        INSERT INTO temperaturas 
        (idpais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    valores = (idpais, timestamp, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer)
    
    cursor.execute(consulta, valores)
    conexion.commit()
    
    id_temperatura = cursor.lastrowid
    
    cursor.close()
    
    return id_temperatura


# ==================== RECUPERACIÓN DE DATOS ====================

def obtener_todos_paises(conexion):
    """
    Obtiene todos los países de la base de datos
    
    Devuelve:
        Lista de diccionarios con los datos de cada país
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


def obtener_pais_por_nombre(conexion, nombre):
    """
    Busca un país por su nombre
    
    Parámetros:
        conexion: conexión a la base de datos
        nombre: nombre del país a buscar
    
    Devuelve:
        Diccionario con los datos del país (o None si no se encuentra)
    """
    cursor = conexion.cursor(dictionary=True)
    
    consulta = """
        SELECT idpais, cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud 
        FROM paises 
        WHERE nombre LIKE %s
    """
    
    cursor.execute(consulta, (f"%{nombre}%",))
    pais = cursor.fetchone()
    
    cursor.close()
    
    return pais


def obtener_pais_por_cca3(conexion, cca3):
    """
    Busca un país por su código cca3
    
    Parámetros:
        conexion: conexión a la base de datos
        cca3: código cca3 del país
    
    Devuelve:
        Diccionario con los datos del país (o None si no se encuentra)
    """
    cursor = conexion.cursor(dictionary=True)
    
    consulta = """
        SELECT idpais, cca2, cca3, nombre, capital, region, subregion, miembroUE, latitud, longitud 
        FROM paises 
        WHERE cca3 = %s
    """
    
    cursor.execute(consulta, (cca3,))
    pais = cursor.fetchone()
    
    cursor.close()
    
    return pais


def obtener_fronteras_pais(conexion, idpais):
    """
    Obtiene todas las fronteras de un país
    
    Parámetros:
        conexion: conexión a la base de datos
        idpais: ID del país
    
    Devuelve:
        Lista de diccionarios con los datos de las fronteras
    """
    cursor = conexion.cursor(dictionary=True)
    
    consulta = """
        SELECT f.idfronteras, f.idpais, f.cca3_frontera, p.nombre as nombre_frontera
        FROM fronteras f
        LEFT JOIN paises p ON f.cca3_frontera = p.cca3
        WHERE f.idpais = %s
    """
    
    cursor.execute(consulta, (idpais,))
    fronteras = cursor.fetchall()
    
    cursor.close()
    
    return fronteras


def obtener_temperatura_mas_reciente(conexion, idpais):
    """
    Obtiene la temperatura más reciente de un país
    
    Parámetros:
        conexion: conexión a la base de datos
        idpais: ID del país
    
    Devuelve:
        Diccionario con los datos de temperatura (o None si no hay registros)
    """
    cursor = conexion.cursor(dictionary=True)
    
    consulta = """
        SELECT t.*, p.nombre, p.capital
        FROM temperaturas t
        JOIN paises p ON t.idpais = p.idpais
        WHERE t.idpais = %s
        ORDER BY t.timestamp DESC
        LIMIT 1
    """
    
    cursor.execute(consulta, (idpais,))
    temperatura = cursor.fetchone()
    
    cursor.close()
    
    return temperatura


def obtener_temperaturas_pais_y_fronteras(conexion, nombre_pais):
    """
    Obtiene la temperatura de un país y de sus países fronterizos
    
    ESTA FUNCIÓN IMPLEMENTA EL PUNTO 3 DEL EJERCICIO:
    "Obtener de la base de datos la temperatura de un país y sus fronterizos 
    a partir de país dado por usuario"
    
    Parámetros:
        conexion: conexión a la base de datos
        nombre_pais: nombre del país
    
    Devuelve:
        Diccionario con:
        - 'pais': datos del país
        - 'temperatura_pais': temperatura del país
        - 'fronteras': lista con datos y temperaturas de países fronterizos
    """
    # 1. Buscar el país por nombre
    pais = obtener_pais_por_nombre(conexion, nombre_pais)
    
    if pais is None:
        return None
    
    # 2. Obtener temperatura del país
    temperatura_pais = obtener_temperatura_mas_reciente(conexion, pais['idpais'])
    
    # 3. Obtener fronteras del país
    fronteras = obtener_fronteras_pais(conexion, pais['idpais'])
    
    # 4. Para cada frontera, obtener datos del país y su temperatura
    lista_fronteras = []
    
    for frontera in fronteras:
        pais_fronterizo = obtener_pais_por_cca3(conexion, frontera['cca3_frontera'])
        
        if pais_fronterizo is not None:
            temperatura_frontera = obtener_temperatura_mas_reciente(conexion, pais_fronterizo['idpais'])
            
            lista_fronteras.append({
                'pais': pais_fronterizo,
                'temperatura': temperatura_frontera
            })
    
    # 5. Devolver todos los datos organizados
    resultado = {
        'pais': pais,
        'temperatura_pais': temperatura_pais,
        'fronteras': lista_fronteras
    }
    
    return resultado


# ==================== EJEMPLO DE USO ====================

def ejemplo():
    """
    Ejemplo de cómo usar las funciones del módulo
    """
    print("=== EJEMPLO DE USO DEL MÓDULO ===\n")
    
    # 1. Conectar a la base de datos
    print("1. Conectando a la base de datos...")
    conexion = conectar_bd()
    print("   ✓ Conexión establecida\n")
    
    # 2. Insertar un país
    print("2. Insertando país de ejemplo (Spain)...")
    id_pais = insertar_pais(
        conexion,
        cca2="ES",
        cca3="ESP",
        nombre="Spain",
        capital="Madrid",
        region="Europe",
        subregion="Southern Europe",
        miembro_ue=True,
        latitud=40.4168,
        longitud=-3.7038
    )
    print(f"   ✓ País insertado con ID: {id_pais}\n")
    
    # 3. Insertar fronteras
    print("3. Insertando fronteras de Spain...")
    fronteras = ["FRA", "PRT", "AND"]
    for frontera in fronteras:
        insertar_frontera(conexion, id_pais, frontera)
    print(f"   ✓ {len(fronteras)} fronteras insertadas\n")
    
    # 4. Insertar temperatura
    print("4. Insertando temperatura...")
    id_temp = insertar_temperatura(
        conexion,
        idpais=id_pais,
        timestamp=datetime.now(),
        temperatura=15.5,
        sensacion=14.0,
        minima=12.0,
        maxima=18.0,
        humedad=65.0,
        amanecer="07:30:00",
        atardecer="18:45:00"
    )
    print(f"   ✓ Temperatura insertada con ID: {id_temp}\n")
    
    # 5. Recuperar todos los países
    print("5. Recuperando todos los países...")
    paises = obtener_todos_paises(conexion)
    print(f"   ✓ Total de países en la BD: {len(paises)}\n")
    
    # 6. Buscar un país por nombre
    print("6. Buscando país 'Spain'...")
    pais = obtener_pais_por_nombre(conexion, "Spain")
    if pais:
        print(f"   ✓ Encontrado: {pais['nombre']} - {pais['capital']}\n")
    
    # 7. Obtener fronteras
    print("7. Obteniendo fronteras de Spain...")
    fronteras = obtener_fronteras_pais(conexion, id_pais)
    print(f"   ✓ Fronteras: {[f['cca3_frontera'] for f in fronteras]}\n")
    
    # 8. Obtener temperatura más reciente
    print("8. Obteniendo temperatura más reciente...")
    temp = obtener_temperatura_mas_reciente(conexion, id_pais)
    if temp:
        print(f"   ✓ Temperatura en {temp['capital']}: {temp['temperatura']}°C\n")
    
    # 9. Obtener temperatura de país y fronteras (PUNTO 3)
    print("9. Obteniendo temperatura de país y fronteras...")
    resultado = obtener_temperaturas_pais_y_fronteras(conexion, "Spain")
    if resultado:
        print(f"   ✓ País: {resultado['pais']['nombre']}")
        if resultado['temperatura_pais']:
            print(f"   ✓ Temperatura: {resultado['temperatura_pais']['temperatura']}°C")
        print(f"   ✓ Fronteras con datos: {len(resultado['fronteras'])}\n")
    
    # 10. Cerrar conexión
    print("10. Cerrando conexión...")
    conexion.close()
    print("    ✓ Conexión cerrada\n")
    
    print("=== FIN DEL EJEMPLO ===")


if __name__ == "__main__":
    # Al ejecutar este archivo directamente, se muestra el ejemplo
    # NOTA: Asegúrate de cambiar la contraseña en CONFIG_DB antes de ejecutar
    print("Para usar este módulo, impórtalo en tu programa principal:")
    print("  import db_module")
    print("  conexion = db_module.conectar_bd()")
    print("\nPara ver un ejemplo completo, descomenta la siguiente línea:\n")
    # ejemplo()