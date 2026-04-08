from kafka import KafkaProducer
import json
import time
import random

matriculas = [
    "12839KLM", "45092TRZ", "94830QWE", "73821XCV", "10923BNM",
    "34567ZXC", "78234QAZ", "39847EDC", "56123RFV", "78401TGB",
    "93218YHN", "87245UJM", "10029IKL", "45903OLP", "88923LKJ",
    "23789MNB", "12048POI", "98347UYT", "47821TRE", "37492WSX",
    "94567EDV", "68345GBH", "15423NHY", "34987UJH", "22019IKM",
    "32048PLK", "40298MNJ", "82930XCD", "74923DFR", "98234WSA",
    "73482JHG", "15390REW", "98234TGY", "40001ZXV", "38201MLK",
    "68492PNM", "38219UIK", "52348OPA", "93484GHK", "76420LUI",
    "62190KJU", "89012TRE", "19384WSD", "80239CDE", "54093LOI",
    "74821JLO", "92384MKL", "28493BGT", "67492NAQ", "58129OMI"
]

topic = "ParkingAlvaro"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    matricula = random.choice(matriculas)

    mensaje = {
        "lector": "ENTRADA2",
        "tipo": "entrada",
        "matricula": matricula
    }

    producer.send(topic, value=mensaje)
    producer.flush()

    print("Mensaje enviado:", mensaje)

    time.sleep(10)