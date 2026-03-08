# UT3 EJERCICIO 2 - ALVARO FERNANDEZ BECERRA 
import requests
import json

# CONFIGURACIÓN

BASE_URL = "https://restcountries.com/v3.1"

# FUNCIONES AUXILIARES
def guardar_json(data, filename):
    """Guarda datos en archivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Guardado: {filename} ({len(data)} registros)")

def cargar_json(filename):
    """Carga datos desde archivo JSON"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# EJERCICIO 1: PAISES CON EURO
print("1. Paises con Euro")
response = requests.get(f"{BASE_URL}/all")
paises = response.json()

paises_euro = []
for pais in paises:
    if 'currencies' in pais:
        for codigo, moneda in pais['currencies'].items():
            if codigo == 'EUR':
                paises_euro.append(pais)
                break

guardar_json(paises_euro, 'paises_euro.json')


# EJERCICIO 2: PAISES CON DOLAR
print("\n2. Obteniendo paises con Dólar...")
paises_dolar = []
for pais in paises:
    if 'currencies' in pais:
        for codigo, moneda in pais['currencies'].items():
            if codigo == 'USD':
                paises_dolar.append(pais)
                break

guardar_json(paises_dolar, 'paises_dolar.json')


# EJERCICIO 3: PAISES QUE HABLAN ESPAÑOL
print("\n3. Obteniendo paises hispanohablantes...")
response = requests.get(f"{BASE_URL}/lang/spa")
paises_espanol = response.json()
guardar_json(paises_espanol, 'paises_espanol.json')


# EJERCICIO 4: PAISES DEL CARIBE
print("\n4. Obteniendo paises del Caribe...")
response = requests.get(f"{BASE_URL}/region/americas")
paises_americas = response.json()
paises_caribe = [p for p in paises_americas if p.get('subregion') == 'Caribbean']
guardar_json(paises_caribe, 'paises_caribe.json')


# EJERCICIO 5: PAISES DE EUROPA 
print("\n5. Obteniendo paises de Europa...")
response = requests.get(f"{BASE_URL}/region/europe")
paises_europa = response.json()
guardar_json(paises_europa, 'paises_europa.json')


# EJERCICIO 6: POAISES DE AMÉRICA 
print("\n6. Obteniendo datos paises de América...")
response = requests.get(f"{BASE_URL}/region/americas?fields=name,currencies,capital,population")
paises_americas_filtrados = response.json()

paises_resumen = []
for pais in paises_americas_filtrados:
    nombre = pais.get('name', {}).get('common', 'N/A')
    
    moneda = 'N/A'
    if 'currencies' in pais:
        for codigo, info in pais['currencies'].items():
            moneda = info.get('name', 'N/A')
            break
    
    capital = pais.get('capital', ['N/A'])[0] if pais.get('capital') else 'N/A'
    poblacion = pais.get('population', 0)
    
    paises_resumen.append({
        'nombre': nombre,
        'moneda': moneda,
        'capital': capital,
        'habitantes': poblacion
    })

guardar_json(paises_resumen, 'paises_americas_resumen.json')


# EJERCICIO 7: DESERIALIZAR EUROPA
print("\n7. Deserializando países de Europa...")
paises_europa_dict = cargar_json('paises_europa.json')
print(f"✅ {len(paises_europa_dict)} países europeos deserializados")


# EJERCICIO 8: CLASE PAÍS + OBJETOS
print("\n8. Creando objetos Pais desde Europa...")

class Pais:
    def __init__(self, nombre, capital, poblacion, area, monedas, idiomas, region):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.area = area
        self.monedas = monedas
        self.idiomas = idiomas
        self.region = region
    
    def __repr__(self):
        return f"Pais('{self.nombre}', poblacion={self.poblacion})"
    
    def info(self):
        print(f"\n--- {self.nombre} ---")
        print(f"Capital: {self.capital}")
        print(f"Población: {self.poblacion:,}")
        print(f"Área: {self.area:,} km²")
        print(f"Monedas: {', '.join(self.monedas)}")
        print(f"Idiomas: {', '.join(self.idiomas)}")

lista_paises = []

for data in paises_europa_dict:
    nombre = data.get('name', {}).get('common', 'N/A')
    capital = data.get('capital', ['N/A'])[0] if data.get('capital') else 'N/A'
    poblacion = data.get('population', 0)
    area = data.get('area', 0)
    
    monedas = []
    if 'currencies' in data:
        for codigo, info in data['currencies'].items():
            monedas.append(info.get('name', codigo))
    
    idiomas = []
    if 'languages' in data:
        idiomas = list(data['languages'].values())
    
    region = data.get('region', 'N/A')
    
    pais = Pais(nombre, capital, poblacion, area, monedas, idiomas, region)
    lista_paises.append(pais)

print(f"{len(lista_paises)} objetos Pais creados")
print("\n📊 Ejemplos:")
for pais in lista_paises[:3]:
    pais.info()

