import requests
from generate_device_interactions.call_generator.generate_calls import generate_device_interaction


def send_interactions(endpoint):
    headers = {"Content-Type": "application/json"}
    try:
        requests.post(
            endpoint,
            json=generate_device_interaction(),
            headers=headers
        )
    except requests.exceptions.RequestException as e:
        print(f"Failed to send batch: {e}")