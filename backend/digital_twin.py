import random
import time

from database import SessionLocal
from models import Sensor


ZONES = [
    "Tank Farm A",
    "Tank Farm B",
    "Boiler Room",
    "Control Room",
    "Loading Bay"
]


def generate_sensor_values():

    return {

        "temperature": round(random.uniform(25, 55), 1),

        "humidity": round(random.uniform(35, 90), 1),

        "pressure": round(random.uniform(1.0, 5.0), 2),

        "gas": round(random.uniform(0, 100), 1)

    }


def run_simulation():

    db = SessionLocal()

    while True:

        for zone in ZONES:

            values = generate_sensor_values()

            sensor = db.query(Sensor).filter(
                Sensor.zone == zone
            ).first()

            if sensor:

                sensor.temperature = values["temperature"]
                sensor.humidity = values["humidity"]
                sensor.pressure = values["pressure"]
                sensor.gas = values["gas"]

            else:

                sensor = Sensor(

                    zone=zone,

                    temperature=values["temperature"],

                    humidity=values["humidity"],

                    pressure=values["pressure"],

                    gas=values["gas"]

                )

                db.add(sensor)

        db.commit()

        print("Updated Digital Twin")

        time.sleep(2)