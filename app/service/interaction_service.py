from dataclasses import asdict
from app.db.model.device import Device
from app.db.model.interaction import Interaction
from app.repository.device_repository import create_device, add_interaction


def device_instance(device, location):
    return Device(
            id=device['id'],
            name=device['name'],
            brand=device['brand'],
            model=device['model'],
            os=device['os'],
            latitude=location['latitude'],
            longitude=location['longitude'],
            altitude_meters=location['altitude_meters'],
            accuracy_meters=location['accuracy_meters']
        )

def interaction_details(interaction):
    return Interaction(
        from_device=interaction['from_device'],
        to_device=interaction['to_device'],
        method=interaction['method'],
        bluetooth_version=interaction['bluetooth_version'],
        signal_strength_dbm=interaction['signal_strength_dbm'],
        distance_meters=interaction['distance_meters'],
        duration_seconds=interaction['duration_seconds'],
        timestamp=interaction['timestamp']
    )

def add_interaction_service(interaction):
    from_device = interaction['from_device']
    to_device = interaction['to_device']
    interaction = interaction_details(interaction)
    interaction = asdict(interaction)
    add_interaction(from_device, to_device, interaction)

def check_duplicate_device(device1, device2):
    return (
        device1.id == device2.id or
        device1.latitude == device2.latitude and device1.longitude == device2.longitude
    )

def process_interaction(data):
    devices = data['devices']
    interaction = data['interaction']
    device1 = devices[0]
    location1 = device1['location']
    device2 = devices[1]
    location2 = device2['location']
    device_instance1 = device_instance(device1, location1)
    device_instance2 = device_instance(device2, location2)
    if not check_duplicate_device(device_instance1, device_instance2):
        create_device(device_instance1)
        create_device(device_instance2)
        add_interaction_service(interaction)