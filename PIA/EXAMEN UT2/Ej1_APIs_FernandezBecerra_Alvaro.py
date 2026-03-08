# EXAMEN UT3 APIS - ÁLVARO FERNÁNDEZ BECERRA

import requests
import json
import xml.etree.ElementTree as ET

URL_ESPECIES ='https://swapi.dev/api/species/'
URL_PELIS = 'https://swapi.dev/api/films/'

def crear_add_especie(lista,nombre,clasificacion,esperanza,pelis):
    """
        Crea un diccionario con los datos necesarios para el apartado 1.
        Luego los añade a una lista de diccionarios.
    """
    dicc = {
    'nombre': nombre,
    'clasificacion': clasificacion,
    'esperanza_vida': esperanza,
    'peliculas': pelis
    }
    lista.append(dicc)

def crear_add_pelicula(lista,titulo,num_ep,fecha,url_peli):
    """
        Crea un diccionario con los datos necesarios para el apartado 2.
        Luego los añade a una lista de diccionarios.
    """
    dicc = {
        'titulo': titulo,
        'num_episodio': num_ep,
        'fecha_lanzamiento': fecha,
        'url_peli': url_peli
    }
    lista.append(dicc)
    
# 1. Obtener información de todas las 'species' que han aparecido en las pelis.
# Se necesita: nombre('name'), clasificacion(`classification`), esperanza media de vida('average_lifespan') y peliculas en las que aparece(lista)

res_especies= requests.get(URL_ESPECIES)
json_especies = res_especies.json()
lista_especies = json_especies['results'] # Lista de diccionarios con cada especie

especies = [] # Lista de diccionarios por cada especie con los datos del apartado 1 

for dic in lista_especies:
    for i in range(len(lista_especies)):
        
        nombre = lista_especies[i]['name']
        clasificacion= lista_especies[i]['classification']
        esperanza_vida = lista_especies[i]['average_lifespan']
        pelis = lista_especies[i]['films']

        crear_add_especie(especies,nombre,clasificacion,esperanza_vida,pelis)

# 2. Para cada pelicula realizar una llamada individual para obtener su info.
# Se necesita: titulo(title), num episodio(episode_id) y fecha de lanzamiento(release_date).

peliculas = [] # Lista de diccionarios por cada pelicula
titulos = [] # Lista de titulos para comprobar si añadir la pelicula a la lista o no.
for i in range (len(especies)):
    for peli in especies[i]['peliculas']: #repetidos

        res_pelicula = requests.get(peli)
        json_pelicula = res_pelicula.json()

        titulo = json_pelicula['title']
        num_ep = json_pelicula['episode_id']
        fecha = json_pelicula['release_date']

        if not titulo in titulos:
            titulos.append(titulo)
            crear_add_pelicula(peliculas,titulo,num_ep,fecha,peli)

print(peliculas)

# 3. Combinar la info y formar diccionario con el formato del .json ejemplo incluyendo todas las especies.
species = []
appearances = []
json_base = {
    "name": "",
    "classification": "",
    "average_lifespan": "",
    "appearances": []
}

for i in range(len(lista_especies)):
    json_base['name'] = lista_especies[i]['nombre']
    json_base['classification'] = lista_especies[i][clasificacion]
    json_base['average_lifespan'] = lista_especies[i][esperanza_vida]
    json_base['appearances'] 

    # Recorrer lista peliculas. Añadir peliculas de cada especie.
    for i in range(len(peliculas)):
        pass

    # Añadir el json a la lista
    species.append(json_base)


try:
    with open('Json_final.json', 'w') as f:
        json.dump(species, f, indent=4)
except Exception as e:
    print(f"Error al crear el archivo JSON: {e}")

# 4. Guardarlo en formato JSON