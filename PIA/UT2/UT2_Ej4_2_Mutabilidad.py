#1
def modificar_entero(x):
    x += 5
    return x

a = 5
resultado = modificar_entero(a)
print("--------EJERCICIO 1 --------------")
print(a)  # ¿Qué valor se imprime?
# El valor
print(resultado)  # ¿Qué valor se imprime?


#2
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

numeros = [1, 2, 3]
agregar_elemento(numeros, 4)
print("--------EJERCICIO 2 --------------")
print(numeros)  # ¿Qué valor se imprime?

#3
def concatenar_y_agregar(texto, numeros, elemento):
    texto += " mundo"
    numeros.append(elemento)
    return texto, numeros

texto = "Hola"
numeros = [1, 2, 3]
concatenar_y_agregar(texto, numeros, 4)
print("--------EJERCICIO 3 --------------")
print(texto)  # ¿Qué valor se imprime?
print(numeros)  # ¿Qué valor se imprime?
#print(resultado_texto) # ¿Qué valor se imprime?
#print(resultado_lista) # ¿Qué valor se imprime?

#4
class MiClase:
    def __init__(self, valor):
        self.valor = valor


def modificar_objeto(objeto):
    objeto.valor += 10
    return objeto

mi_objeto = MiClase(5)
modificar_objeto(mi_objeto)
print("--------EJERCICIO 4 --------------")
print(mi_objeto.valor)  # ¿Qué valor se imprime?

#5
elemento_global = 5

def agregar_elemento_global(lista):
    global elemento_global
    lista.append(elemento_global)
    elemento_global += 1
    return lista

numeros = [1, 2, 3]
agregar_elemento_global(numeros)
print("--------EJERCICIO 5 --------------")
print(numeros)  # ¿Qué valor se imprime?
print(elemento_global)  # ¿Qué valor se imprime?

#6
def modificar_mezcla(x, lista):
    x *= 2
    #funcion que cambia el orden de los elementos de la lista
    lista.reverse() 
    return x, lista

a = 10
numeros = [4, 5, 6]
resultado_a, resultado_lista = modificar_mezcla(a, numeros)
print("--------EJERCICIO 6 --------------")
print(a)  # ¿Qué valor se imprime?
print(numeros)  # ¿Qué valor se imprime?
print(resultado_a)  # ¿Qué valor se imprime?
print(resultado_lista)  # ¿Qué valor se imprime?

#7
def modificar_por_indice(lista, indice, valor):
    if indice < len(lista):
        lista[indice] = valor
    return lista

numeros = [1, 2, 3, 4]
modificar_por_indice(numeros, 2, 99)
print("--------EJERCICIO 7 --------------")
print(numeros)  # ¿Qué valor se imprime?

#8
class Contenedor:
    def __init__(self, contenido):
        self.contenido = contenido

def cambiar_contenido(contenedor, nuevo_contenido):
    contenedor.contenido = nuevo_contenido
    nuevo_contenido += " Contenido"
    return nuevo_contenido

mi_contenedor = Contenedor("Antiguo")
nuevo_contenido = cambiar_contenido(mi_contenedor, "Nuevo")
print("--------EJERCICIO 8 --------------")
print(mi_contenedor.contenido)  # ¿Qué valor se imprime?
print(nuevo_contenido)  # ¿Qué valor se imprime?

#9
class Contador:
    valor = 10  # Atributo de clase

    def __init__(self, contador_pasado=0):
        self.contador = contador_pasado
        valor += 1

mi_contador = Contador(0)
mi_contador1 = Contador(10)

mi_contador.valor

def incrementar_contador():
    global Contador
    Contador.valor += 1
    return Contador.valor

incrementar_contador()
print("--------EJERCICIO 9 --------------")
print(Contador.valor)  # ¿Qué valor se imprime?
