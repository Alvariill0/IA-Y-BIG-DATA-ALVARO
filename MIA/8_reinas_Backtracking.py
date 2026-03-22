def es_seguro(tablero, columna, fila):
    """
    Comprueba si es seguro colocar una reina en (columna, fila)
    respecto a las reinas ya colocadas en columnas anteriores.
    """
    for col_anterior in range(columna):
        fila_anterior = tablero[col_anterior]
        
        # Misma fila (no debería pasar si colocamos fila distinta)
        if fila_anterior == fila:
            return False
        
        # Misma diagonal
        if abs(fila_anterior - fila) == abs(col_anterior - columna):
            return False
    
    return True

def backtracking_8_reinas(tablero, columna):
    """
    Coloca reinas columna por columna usando backtracking.
    tablero[col] = fila donde está la reina en esa columna.
    """
    # Caso base: hemos colocado las 8 reinas
    if columna == 8:
        return True  # Solución encontrada
    
    # Probar todas las filas posibles para esta columna
    for fila in range(1, 9):  # filas 1 a 8
        if es_seguro(tablero, columna, fila):
            # Colocar reina
            tablero[columna] = fila
            
            # Recursión: intentar siguiente columna
            if backtracking_8_reinas(tablero, columna + 1):
                return True
            
            # Backtrack: quitar reina si no funcionó
            tablero[columna] = 0  # marcar como vacío
    
    return False  # No hay solución desde esta columna

def imprimir_tablero(tablero):
    """Imprime el tablero con 'Q' para reinas."""
    for fila in range(1, 9):
        linea = ""
        for col in range(8):
            if tablero[col] == fila:
                linea += " Q"
            else:
                linea += " ."
        print(linea)
    print()

def resolver_8_reinas():
    """Función principal."""
    tablero = [0] * 8  # tablero[columna] = fila de la reina
    
    if backtracking_8_reinas(tablero, 0):
        print("¡Solución encontrada!")
        print("Posiciones (columna:fila):", tablero)
        imprimir_tablero(tablero)
    else:
        print("No hay solución (imposible con 8 reinas)")

if __name__ == "__main__":
    resolver_8_reinas()
