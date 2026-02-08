# api_modulo.py - Modulo API Weathermap - ÁLVARO FERNANDEZ BECERRA
import requests
import json
import xml.etree.ElementTree as ET
import bd_modulo
from datetime import datetime

API_KEY = "fa905b4ca52cfdbb2ed4d595dd07d816"
URL_BASE = "https://api.openweathermap.org/data/2.5/weather"

def obtener_temperaturas_todos_paises():
    """Obtiene las temperaturas de todas las capitales guardadas en la BD.

    - La primera mitad de paises se deben tratar en JSON y la otra en XML

    - Para JSON usamos `r.json()` que devuelve un diccionario.
    - Para XML usando la libreria `xml.etree.ElementTree.fromstring` parsea el texto y devuelve
    un arbol. Permite buscar en cada nodo con `find()` y leer atributos con `get()`.
    """
    conexion = bd_modulo.conectar_bd()
    paises = bd_modulo.obtener_todos_paises(conexion)
    if not paises:
        print("No hay países en la base de datos")
        conexion.close()
        return

    print(f"TOTAL: {len(paises)} países")
    
    mitad = len(paises) // 2  
    
    for i in range(len(paises)):
        pais = paises[i]
        print(f"\n{i+1}. {pais['nombre']}")
        
        try:
            capital = pais['capital']
            cca2 = pais['cca2'].lower()
            
            if not capital:
                # Saltar si no hay capital
                continue
            
            if i < mitad:
                # Primera mitad de paises en JSON
                print(" MitadJSON")
                url = f"{URL_BASE}?q={capital},{cca2}&appid={API_KEY}&units=metric"
                r = requests.get(url)
                datos = r.json()
                
                temperatura = datos['main']['temp']
                sensacion = datos['main']['feels_like']
                minima = datos['main']['temp_min']
                maxima = datos['main']['temp_max']
                humedad = datos['main']['humidity']

                # sys.sunrise y sys.sunset vienen como timestamps, hay que convertir a hora
                amanecer = datetime.fromtimestamp(datos['sys']['sunrise']).time().strftime('%H:%M:%S')
                atardecer = datetime.fromtimestamp(datos['sys']['sunset']).time().strftime('%H:%M:%S')
                
            else:
                # Segunda mitad de paises en XML
                print(" Mitad XML")
                url = f"{URL_BASE}?q={capital},{cca2}&appid={API_KEY}&units=metric&mode=xml"
                r = requests.get(url)
                raiz = ET.fromstring(r.text)
                
                temperatura = float(raiz.find('.//temperature').get('value'))
                sensacion = float(raiz.find('.//feels_like').get('value'))
                minima = float(raiz.find('.//temperature').get('min'))
                maxima = float(raiz.find('.//temperature').get('max'))
                humedad = float(raiz.find('.//humidity').get('value'))
                sun = raiz.find('.//city/sun') or raiz.find('.//sun')
                # Si no transformaramos se imprimiria:
                amanecer_no = sun.get('rise')
                atardecer_no = sun.get('set')
                print(f"  Amanecer (raw): {amanecer_no}, Atardecer (raw): {atardecer_no}")

                amanecer = sun.get('rise').split('T')[1][:8]
                atardecer = sun.get('set').split('T')[1][:8]
            
            # GUARDAR BD
            ahora = datetime.now()
            bd_modulo.insertar_temperatura(conexion, pais['idpais'], ahora, temperatura, sensacion, minima, maxima, humedad, amanecer, atardecer)
            print(f"{temperatura}°C")
            
        except Exception as e:
            print(e)
    
    conexion.close()
