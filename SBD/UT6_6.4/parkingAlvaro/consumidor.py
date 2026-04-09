from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# Topic obligatorio con el nombre del alumno.
topic = "ParkingAlvaro"

# Conectamos con Kafka y leemos mensajes desde el principio del topic.
# value_deserializer convierte los mensajes JSON de Kafka en diccionarios Python.
consumer = KafkaConsumer(
    topic,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="grupo_parking_alvaro",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

# Conectamos con MongoDB local.
# La base de datos y la colección deben llamarse ParkingAlvaro.
client = MongoClient("mongodb://localhost:27017")
db = client["ParkingAlvaro"]
collection = db["ParkingAlvaro"]

print("Consumidor iniciado. Esperando mensajes...")

# Bucle infinito para ir leyendo mensajes del topic y guardarlos en MongoDB.
for mensaje in consumer:
    dato = mensaje.value
    collection.insert_one(dato)
    print("Insertado en MongoDB:", dato)