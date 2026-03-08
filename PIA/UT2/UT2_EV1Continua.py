# Búsqueda de nombres y teléfonos en un diccionario - Alvaro Fernandez Becerra

# Escribe un programa que tenga un diccionario de contactos hardcodeado
# (no hay que pedir al usuario que introduzca los datos, sino que los escribimos directamente en el código).
#  Las claves del diccionario son nombres de personas y los valores son sus números de teléfono.

# El programa da la opción al usuario de introducir un texto de búsqueda y realiza la búsqueda para
# ese texto tanto en los nombres como en los números de teléfono. Si se encuentra una coincidencia por nombre, el programa devuelve por pantalla el número de teléfono asociado. 
# Si se encuentra una coincidencia por teléfono, el programa devuelve por pantalla el nombre del usuario. Si no se encuentra ninguna coincidencia se indica por pantalla.

# El programa continúa ofreciendo una búsqueda al usuario hasta que este introduce la palabra “salir”.

CONTACTOS = {
    "Alvaro": "123456789",
    "Maria": "987654321",
    "Juan": "123123123",
    "Ana": "321321321"
}

def buscar_texto(texto):
    for nombre, telefono in CONTACTOS.items():
        if texto in nombre:
            print(f"El número de teléfono de es {telefono}.")
            return
        elif texto in telefono:
            print(f"El nombre asociado al número es {nombre}.")
            return
    print("No se ha encontrado ninguna coincidencia.")

while True:
    texto = input("Introduce un texto de búsqueda (o 'salir' para terminar): ")
    if texto == "salir":
        break
    buscar_texto(texto)