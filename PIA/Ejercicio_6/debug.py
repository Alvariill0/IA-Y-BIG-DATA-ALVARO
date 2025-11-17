try:
    gen = str(input("Que género quieres consultar (Femenino/Masculino)? ").strip().lower())
    if gen not in ("femenino", "masculino"):
        raise ValueError("Género no válido. Debe ser 'Femenino' o 'Masculino'.")
    
    with open('Ejercicio_6\\alturas.csv', 'r') as fich:
        next(fich)
        total_altura = 0 # *pulgadas
        cantidad = 0

        for linea in fich:
            if linea.split(',')[0].strip().lower() == gen:
                total_altura += float(linea.split(',')[1])
                cantidad += 1
        if cantidad > 0:
            total_altura = total_altura * 0.0254  # metrps
            media = total_altura / cantidad
            
except FileNotFoundError:
    print("Error:  fichero no encontrado.")
else:
    print(f"La altura promedio de {gen} es {media:.2f} metros.")
finally:
    pass