from typing import List
from app.db.neo4j_database import driver
from app.db.query.analysis_query import query_bluetooth_connections, query_devices_by_signal_strength, \
    query_count_connected_devices, query_determine_direct_connection_between_two_devices, \
    query_most_recent_interaction_repo


def find_bluetooth_connections() -> List[dict]:
    with driver.session() as session:
        query = query_bluetooth_connections
        result = session.run(query)
        return [
            {
                "from_device": record["from_device"],
                "to_device": record["to_device"],
                "path_length": record["path_length"]
            } for record in result
        ]

def devices_by_signal_strength() -> List[dict]:
   with driver.session() as session:
       query = query_devices_by_signal_strength
       result = session.run(query).data()
       return result

def count_connected_devices(device_id: str) -> int:
    with driver.session() as session:
        query = query_count_connected_devices
        result = session.run(query, device_id=device_id)
        record = result.single()
        return record["connected_count"] if record else 0

def determine_direct_connection_between_two_devices(device_id_1: str, device_id_2: str) -> bool:
    with driver.session() as session:
        query = query_determine_direct_connection_between_two_devices
        result = session.run(query, device_id_1=device_id_1, device_id_2=device_id_2)
        record = result.single()
        return record["connection_count"] > 0

def get_most_recent_interaction_repo(device_id: str) -> dict:
   with driver.session() as session:
       query = query_most_recent_interaction_repo
       params = {"device_id": device_id}
       result = session.run(query, params)
       record = result.single()
       most_interaction = record["most_interaction"]
       return dict(most_interaction) if record else {"error" : "not found interactions"}