from dataclasses import asdict
from dis import Instruction

from app.db.model.device import Device
from app.db.model.interaction import Interaction
from app.repository.device_repository import create_device, add_interaction


def device_instance(device, location):
    return Device(
            id=device['id'],
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
        method=interaction['method'],
        bluetooth_version=interaction['bluetooth_version'],
        signal_strength_dbm=interaction['signal_strength_dbm'],
        distance_meters=interaction['distance_meters'],
        duration_seconds=interaction['duration_seconds'],
        timestamp=interaction['timestamp']
    )

def process_interaction(data):
        # Parse and store interaction data
        for d in data:
            devices = d['devices']
            interaction = d['interaction']

            device1 = devices[0]
            location1 = device1['location']
            device2 = devices[1]
            location2 = device2['location']
            device_instance1 = device_instance(device1, location1)
            device_instance2 = device_instance(device2, location2)
            create_device(device_instance1)
            create_device(device_instance2)

            for k in interaction:
                print(type(interaction[k]))
            #Add interaction
            from_device = interaction['from_device']
            to_device = interaction['to_device']
            interaction = interaction_details(interaction)
            interaction = asdict(interaction)
            add_interaction(from_device, to_device, interaction)