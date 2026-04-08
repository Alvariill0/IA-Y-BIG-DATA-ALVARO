from kafka import KafkaProducer
import json
import time

topic = "Actividad1Alvaro"
nombre = "Alvaro"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(1, 21):
    mensaje = f"{nombre}{i}"
    producer.send(topic, value=mensaje)
    producer.flush()
    print(f"Enviado: {mensaje}")
    time.sleep(5)

producer.close()