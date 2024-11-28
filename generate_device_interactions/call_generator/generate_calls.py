from faker import Faker
import random

fake = Faker()

# Generate random device data
def generate_device():
    return {
        "id": fake.uuid4(),
        "name": fake.first_name(),
        "brand": fake.company(),
        "model": fake.word().capitalize() + " " + fake.word().capitalize(),
        "os": fake.word().capitalize() + "OS " + f"{random.randint(1, 15)}.{random.randint(0, 9)}",
        "location": {
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude()),
            "altitude_meters": random.randint(0, 5000),
            "accuracy_meters": random.randint(1, 50)
        }
    }

devices = [generate_device() for _ in range(0, 30)]


def generate_device_interaction():
    random_devices = random.sample(devices, 2)
    device_1 = random_devices[0]
    device_2 = random_devices[1]
    # Generate random interaction data
    interaction = {
        "from_device": device_1["id"],
        "to_device": device_2["id"],
        "method": random.choice(["Bluetooth", "WiFi", "NFC"]),
        "bluetooth_version": f"{random.randint(4, 5)}.{random.randint(0, 3)}",
        "signal_strength_dbm": random.randint(-90, -30),
        "distance_meters": round(random.uniform(0.5, 20.0), 2),
        "duration_seconds": random.randint(1, 300),
        "timestamp": fake.iso8601()
    }

    # Combine into a final JSON structure
    data = {
        "devices": [device_1, device_2],
        "interaction": interaction
    }

    return data