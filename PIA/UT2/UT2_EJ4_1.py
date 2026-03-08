#1
def modificar_entero(x):
    x += 5
    return x

a = 5
resultado = modificar_entero(a)
print(a) # Qué valor imprime?
print(resultado) # Qué valor imprime?


#2
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

numeros = [1, 2, 3]
agregar_elemento(numeros, 4)
print(numeros) # Qué valor imprime?

#3
def concatenar_y_agregar(s, lista,elemento):
    s += " Mundo"
    lista.append(elemento)
    return s, lista

texto = "Hola"
numeros = [1, 2, 3]
resultado_texto, resultado_lista = concatenar_y_agregar(texto, numeros, 4)
print(texto) # Qué valor imprime?
print(numeros) # Qué valor imprime?
print(resultado_texto) # Qué valor imprime?
print(resultado_lista) # Qué valor imprime?

#4
class miClase:
    def __init__(self, valor):
        self.valor = valor

def modificar_objeto(objeto):
    objeto.valor += 10
    return objeto

mi_objeto = miClase(5)
modificar_objeto(mi_objeto)
print(mi_objeto.valor) # Qué valor imprime?


# 5
elemento_global = 5
def agregar_elemento_global(lista):
    global elemento_global
    lista.append(elemento_global)
    elemento_global += 1
    return lista

numeros = [1, 2, 3]
agregar_elemento_global(numeros)
print(numeros) # Qué valor imprime?
print(elemento_global) # Qué valor imprime?

#6
def modificar_mezcla(x, lista):
    x *= 2
    # funcion que cambia el orden de los elementos de la lista
    lista.reverse()
    return x, lista

a = 10
numeros = [4, 5, 6]
resultado_a, resultado_lista = modificar_mezcla(a, numeros)
print(a) # Qué valor imprime?
print(numeros) # Qué valor imprime?
print(resultado_a) # Qué valor imprime?
print(resultado_lista) # Qué valor imprime?

#7
def modificar_por_indice(lista, indice, valor):
    if indice < len(lista):
        lista[indice] = valor
    return lista

numeros = [1, 2, 3, 4]
modificar_por_indice(numeros, 2, 99)
print(numeros) # Qué valor imprime?