tabla_percepcion_accion = {
    (0, 0, 0): "Avanzar",                              # Todo despejado
    (1, 0, 0): "Detener y Girar a la Derecha",        # Obstáculo adelante
    (0, 1, 0): "Girar a la Derecha",                  # Obstáculo izquierda
    (0, 0, 1): "Girar a la Izquierda",                # Obstáculo derecha
    (1, 1, 0): "Detener y Girar a la Derecha",        # Obstáculos adelante e izquierda
    (0, 1, 1): "Avanzar",                              # Solo laterales bloqueados
    (1, 0, 1): "Detener y Girar a la Izquierda",      # Obstáculos adelante y derecha
    (1, 1, 1): "Detener"                               # Todos los sensores bloqueados
}
#-	Simula el recorrido del AGV con una lista de tuplas que representen las percepciones (mínimo 10).
# Si hay una percepcion que no esta en la tabla, muestra: Detener.
percepciones = [
    (0, 0, 0),  # Todo despejado
    (1, 0, 0),  # Obstáculo adelante
    (0, 1, 0),  # Obstáculo izquierda
    (0, 0, 1),  # Obstáculo derecha
    (1, 1, 0),  # Obstáculos adelante e izquierda
    (0, 1, 1),  # Solo laterales bloqueados
    (1, 0, 1),  # Obstáculos adelante y derecha
    (1, 1, 1),  # Todos los sensores bloqueados
    (0, 0, 0),  # Todo despejado nuevamente
    (1, 0, 1),   # Obstáculos adelante y derecha
    # ejemplo de percepcion que no esta en la tabla: detener
    (1, 1, 1)   # Todos los sensores bloqueados 
]

# Para cada percepcion del recorrido, mostrar la accion correspondiente
for percepcion in percepciones:
    accion = tabla_percepcion_accion.get(percepcion, "Detener")
    print(f"Percepción: {percepcion} -> Acción: {accion}")