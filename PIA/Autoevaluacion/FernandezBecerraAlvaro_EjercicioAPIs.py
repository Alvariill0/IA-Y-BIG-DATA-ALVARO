# EJERCICIO AUTOEVALUACION APIS - ALVARO FERNANDEZ BECERRA
import mysql.connector
import json
import requests
from datetime import datetime
import os

URL="https://api.frankfurter.app/latest"
URL2="https://api.frankfurter.app/currencies"

#1 - 1.	Realiza una llamada a la API para obtener los tipos de cambio del dólar.
url = "https://api.frankfurter.dev/v1/latest?base=USD"
try:
    res_dolar = requests.get(url)
    datos_dolar = res_dolar.json()
    # Recorrer y mostrar:
    print("-- MONEDA BASE: DOLAR --\n TIPOS DE CAMBIO:")
    ratios = dict(datos_dolar['rates'])

    for clave,valor in ratios.items():
        print(f"Moneda: {clave}, cambio a USD: {valor}")

except Exception as e:
    print(f"Error al obtener datos del dólar: {e}")

#2 - 2.	Realiza una llamada a la API para obtener la lista de los nombres completos de las monedas
try: 
    res_monedas = requests.get(URL2)
    datos_monedas = res_monedas.json()
    monedas = []
    datos_monedas = dict(datos_monedas)
    for nombre in datos_monedas.values():
        monedas.append(nombre)
    print(f"\n-- LISTA DE MONEDAS --\n {monedas}")

except Exception as e:
    print(f"Error al obtener datos de las monedas: {e}")

#3 - 3.	Combina la información de ambas APIs para formar un JSON con el siguiente formato extendido para todas las monedas y guárdalo. 
# Cogemos solo 'base' y 'date' de los datos del dolar.
# Recorriendo 'rates' del dolar sacar codigo y ratio.
# Recorriendo datos_monedas sacar nombre completo
# Bucle crear diccionario y añadirlo a la lista de 'currencies'

datos_dolar = res_dolar.json()
datos_monedas = res_monedas.json()

json_base= {
    "base": datos_dolar['base'],
    "date": datos_dolar['date'],
    "currencies": []
}
currencies = []

ratios = dict(datos_dolar['rates'])
nombres_monedas = dict(datos_monedas)

for clave1,ratio in ratios.items():
    for clave2, nombre_completo in nombres_monedas.items():
        dicc= {}
        #En principio los codigos estan siempre en el mismo orden
        if clave1 == clave2:
            dicc['code'] = clave2
            dicc['name'] = nombre_completo
            dicc['rate'] = ratio
            # añadir a la lista de currencies.
            currencies.append(dicc)

json_base['currencies'] = currencies
print("\n-- JSON FINAL --\n")
print(json_base)

# Crear archivo json:
try:
    with open('Json_final.json', 'w') as f:
        json.dump(json_base, f, indent=4)
except Exception as e:
    print(f"Error al crear el archivo JSON: {e}")

