def procesar_ventas(fichero, producto_nombre):
    with open(fichero, 'r' ) as fich:
        # Muevo el puntero despues de las cabeceras:
        next(fich)
        # Leer lineas del fichero
        contenido = fich.readlines()
        # Diccionario producto y ingreso total(cantidad x valor unitario).
        producto = {}
        # Recorrer el contenido
        for linea in contenido:
            datos = linea.strip().split(',')
            if datos[0] == producto_nombre:
                #Guardar datos producto si coindice con el nombre a filtrar
                nombre_producto = datos[0]
                cantidad = int(datos[1])
                precio = float(datos[2])
                #Si ya esta en el diccionario, se actualiza el valor. Si no, se añade.
                if nombre_producto in producto.keys():
                    producto[nombre_producto] += cantidad*precio
                else:
                    producto[nombre_producto] = cantidad*precio
        fich.close()
        #Si existe el producto, se devuelve el diccionario. Si no, un mensaje.
        if not producto:
            return f'El producto {producto_nombre} no se ha encontrado.'
        else:
            return producto[nombre_producto]
fichero = 'prueba.csv'
procesar_ventas(fichero, 'producto10')

