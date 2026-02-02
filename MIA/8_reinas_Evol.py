import random

N = 8
MAX_FITNESS = 28
TAM_POBLACION = 80
MAX_GENERACIONES = 1000
PROB_MUTACION_BASE = 0.2


def generar_individuo():
    return [random.randint(1, N) for _ in range(N)]


def generar_poblacion(tamano):
    return [generar_individuo() for _ in range(tamano)]


def fitness(tablero):
    conflictos = 0
    for i in range(N):
        for j in range(i + 1, N):
            if tablero[i] == tablero[j]:
                conflictos += 1
            elif abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1
    return MAX_FITNESS - conflictos


def cruce(p1, p2):
    punto = random.randint(1, N - 2)
    return p1[:punto] + p2[punto:]


def mutar(tablero, prob):
    if random.random() < prob:
        col = random.randint(0, N - 1)
        tablero[col] = random.randint(1, N)


def mostrar_tablero(tablero):
    for fila in range(1, N + 1):
        for col in range(N):
            print("Q" if tablero[col] == fila else ".", end=" ")
        print()
    print()


def algoritmo_evolutivo():
    poblacion = generar_poblacion(TAM_POBLACION)
    mejor_fitness_global = 0
    generaciones_sin_mejora = 0

    for gen in range(1, MAX_GENERACIONES + 1):
        poblacion.sort(key=fitness, reverse=True)
        mejor = poblacion[0]
        fit = fitness(mejor)

        print(f"Generación {gen}: mejor fitness = {fit}")

        if fit > mejor_fitness_global:
            mejor_fitness_global = fit
            generaciones_sin_mejora = 0
        else:
            generaciones_sin_mejora += 1

        if fit == MAX_FITNESS:
            print("Solución perfecta encontrada:")
            mostrar_tablero(mejor)
            return mejor

        # Mutación adaptativa
        prob_mut = PROB_MUTACION_BASE + (generaciones_sin_mejora * 0.01)

        # Selección de élite
        elite = poblacion[:10]
        nueva_poblacion = elite.copy()

        while len(nueva_poblacion) < TAM_POBLACION:
            p1, p2 = random.sample(elite, 2)
            hijo = cruce(p1, p2)
            mutar(hijo, prob_mut)
            nueva_poblacion.append(hijo)

        # Reinicio parcial si está estancado
        if generaciones_sin_mejora > 100:
            nueva_poblacion[-20:] = generar_poblacion(20)
            generaciones_sin_mejora = 0

        poblacion = nueva_poblacion

    print("No se alcanzó una solución perfecta.")
    return mejor


if __name__ == "__main__":
    solucion = algoritmo_evolutivo()
    print("Mejor solución encontrada:", solucion)
    print("\nTablero final:")
    mostrar_tablero(solucion)
