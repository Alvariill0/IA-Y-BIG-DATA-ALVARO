# Algoritmo movimiento con sensores - Álvaro Fernandez Becerra
movimientos = {
    # (Delante(S1), Izquierda (S2), Derecha(S3)) : Acción
    (0,0,0): "Avanzar",
    (1,0,0): "Detenerse y girar a la izquierda / derecha",
    (0,1,0): "Girar a la derecha",
    (0,0,1): "Girar a la izquierda",
    (1,1,0): "Detenerse y girar a la derecha",
    (0,1,1): "Avanzar",
    (1,0,1): "Detenerse y girar a la izquierda",
    (1,1,1): "Detenerse por completo /  Doble giro",
}

while True:
    try:
        print("Ve indicando si tienes obstaculos. Responde con 1(sí) o 0(no):")
        s1 = int(input("Tienes obstaculos delante? "))
        s2 = int(input("Tienes obstaculos a la izquierda? "))
        s3 = int(input("Tienes obstaculos a la derecha? "))

        accion = movimientos.get((s1, s2, s3), "Combinación no encontrada. Detenerse.")
        print(f"Acción sugerida: {accion}")

        if s1 == 1 and s2 == 1 and s3 == 1:
            res = input("No puedes continuar. Hacer doble giro y seguir? (si/no)")
            if res.lower() == "no":
                break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa 1 o 0.")
