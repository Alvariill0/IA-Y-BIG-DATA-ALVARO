'''
presupuesto = 0
while True:
    precio = float(input("Introduce un precio (0 para finalizar): "))
    if precio == 0:
        print("Final, tu presupuesto es:", presupuesto)
        break
    elif precio > 200:
        print("Te has pasado de presupuesto.")
        break
    else:
        presupuesto += precio
        print("Precio añadido:", presupuesto)
# Prueba diccionario
'''
# los diccionarios pueden tener valores que a su vez sean diccionarios
diccionario3={"alumno1":{"nombre":"Juan","apellidos":["Pérez","López"],"notas":[5,3,2],"familiares":{}},
            "alumno2":{"nombre":"Paco","apellidos":"Jonhson","expulsiones":3},
            "alumno3":{"nombre":"María","apellidos":["Sanchez","López"],"matriculasH":5},
            "alumno4":[]}
# Mostrar datos de todos los alumnos
x = 'Hola hola hola hola'
x = x.count('hola') +1
print(x)
