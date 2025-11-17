# Algoritmo diagnostico impresora - Álvaro Fernandez Becerra

def preguntar(pregunta):
    while True:
        respuesta = input(pregunta + " (Si/No): ").lower()
        if respuesta in ['si', 'no']:
            return respuesta
        print("Por favor, escribe 'Si' o 'No'.")

def diagnostico_impresora():
    p1 = preguntar("(P1) ¿Cable de alimentación conectado?")
    if p1 == 'no':
        print("C1: Problema de Alimentación Eléctrica")
        return

    p2 = preguntar("(P2) ¿Hay papel?")
    if p2 == 'no':
        print("C3: Reponer Consumibles (Papel)")
        return

    p3 = preguntar("(P3) ¿Tóner bajo?")
    if p3 == 'si':
        print("C2: Reponer Consumibles (Tóner/Cartucho)")
        return

    p4 = preguntar("(P4) ¿Documento pausado o error en la cola de impresión?")
    if p4 == 'si':
        print("C4: Solucionar Problema de Software/Cola")
        return

    p5 = preguntar("(P5) ¿Luz de error/alerta parpadea?")
    if p5 == 'si':
        print("C6: Fallo Genérico de Hardware/Mecánico")
        return

    p6 = preguntar("(P6) ¿Atasco de papel reportado?")
    if p6 == 'si':
        print("C5: Solucionar Atasco Físico")
        return

    print("C7: Funcionamiento normal")


diagnostico_impresora()