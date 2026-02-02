N = 8  # tamaño del tablero

def es_seguro(tablero, columna_actual):
    """
    Comprueba si la reina colocada en la columna_actual
    entra en conflicto con las anteriores
    """
    for col_anterior in range(columna_actual):
        # Mismo fila
        if tablero[col_anterior] == tablero[columna_actual]:
            return False
        
        # Misma diagonal
        if abs(tablero[col_anterior] - tablero[columna_actual]) == \
            abs(col_anterior - columna_actual):
            return False

    return True


def resolver_8_reinas(tablero, columna, soluciones):
    # Caso base: si hemos colocado las 8 reinas
    if columna == N:
        soluciones.append(tablero.copy())
        return

    # Probar todas las filas en la columna actual
    for fila in range(N):
        tablero[columna] = fila

        if es_seguro(tablero, columna):
            resolver_8_reinas(tablero, columna + 1, soluciones)
        # Si no es seguro, automáticamente se prueba la siguiente fila


def mostrar_tablero(tablero):
    """
    Muestra el tablero de forma visual
    """
    for fila in range(N):
        for col in range(N):
            if tablero[col] == fila:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Programa principal
tablero = [-1] * N
soluciones = []

resolver_8_reinas(tablero, 0, soluciones)

print(f"Número total de soluciones: {len(soluciones)}\n")

# Mostrar la primera solución como ejemplo
print("Ejemplo de solución:\n")
mostrar_tablero(soluciones[0])
