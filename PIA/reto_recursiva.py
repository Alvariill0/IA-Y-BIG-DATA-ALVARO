diccionario3 = {
    'alumno1': {'Nombre': 'Ana', 'Edad': 20, 'Carrera': 'Ingeniería', 'notas': [8, 9, 7]},
    'alumno2': {'Nombre': 'Luis', 'Edad': 22, 'Carrera': 'Medicina', 'familiares':{}},
    'alumno3': {'Nombre': 'Marta', 'Edad': 21, 'Carrera': 'Derecho', 'notas': [9, 8, 10]}
}

if isinstance(diccionario3) == dict:
    for clave, valor in diccionario3:
        print(clave, ": ", valor)
elif isinstance(diccionario3) == list:
    for indice in len(diccionario3):
        print("Elemento ", indice, ": ",diccionario3[indice])
'''
A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to
check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.
'''
#Codigo recursivo para recorrer diccionarios y su contenido (sea diccionario o lista)