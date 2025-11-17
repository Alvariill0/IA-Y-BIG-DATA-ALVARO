# Diccionario animales : 
animales = {
    "pregunta": "¿Tiene plumas?",
    "si": {
        "pregunta": "¿Es un gorrión?",
        "si": {"animal": "gorrión"},
        "no": {"animal": None}   
    },
    "no": {
        "pregunta": "¿Tiene 4 patas?",
        "si": {
            "pregunta": "¿Es un perro?",
            "si": {"animal": "perro"},
            "no": {"animal": None}
        },
        "no": {
            "pregunta": "¿Vive en el mar?",
            "si": {
                "pregunta": "¿Es una sardina?",
                "si": {"animal": "sardina"},
                "no": {"animal": None}
            },
            "no": {"animal": None}
        }
    }
}


# Funcion para preguntas si/no
def preguntar_si_no(texto):
    while True:
        respuesta = input(texto).lower()
        if respuesta in ("si", "no"):
            return respuesta
        print("Responde con si o no.")


# Recorrer el arbol y preguntar
def jugar(nodo):
    # mientras existe pregunta en el diccionario sigue preguntando
    while "pregunta" in nodo:
        r = preguntar_si_no(nodo["pregunta"])
        if r == "si":
            nodo = nodo["si"]
        else:
            nodo = nodo["no"]

    # devolver el nodo del que salimos
    return nodo


# Añadir preguntas y animales al diccionario
def aprender(nodo, animal_fallado):
    print("Perdi")
    mejorar = preguntar_si_no("Quieres ayudarme a mejorar? (si/no):")

    if mejorar == "no":
        print("Chao pescao.")
        return

    animal_correcto = input("En que animal estabas pensando?: ")

    # Pedimos una pregunta nueva, debe ser SI para el animal correcto y NO para el fallado
    print("Escribe una pregunta cuya respuesta sea 'si' para tu animal")
    print(f"y 'no' para el animal que yo dije: {animal_fallado}")
    nueva_pregunta = input("Nueva pregunta: ")

    # Cambiar nodo a pregunta
    nodo["pregunta"] = nueva_pregunta
    nodo["si"] = {"animal": animal_correcto}      # caso verdadero
    nodo["no"] = {"animal": animal_fallado}       # caso falso

    # Cambiar el nodo animal porque ahora es una pregunta
    del nodo["animal"]

    print("Animal añadido")


# PROGRAMA PRINCIPAL
print("Piensa en un animal...")

while True:
    nodo = jugar(animales)

    animal_propuesto = nodo["animal"]

    if animal_propuesto is not None:
        acierto = preguntar_si_no(f"¿Es un {animal_propuesto}?")
        # Comprobar si acierta, si no, aprender
        if acierto == "si":
            print("He ganado")
        else:
            aprender(nodo, animal_propuesto)

    else:
        aprender(nodo, "desconocido")
        
    # preguntar si quieren jugar otra vez
    seguir = preguntar_si_no("¿Quieres jugar otra vez?")
    if seguir == "no":
        print("Hasta luego!")
        break