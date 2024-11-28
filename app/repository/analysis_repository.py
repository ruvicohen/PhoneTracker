from app.db.neo4j_database import driver


def find_bluetooth_connections():
    with driver.session() as session:
        query = """
        MATCH path = (d1:Device)-[r:Interaction*]->(d2:Device)
        WHERE all(rel IN r WHERE rel.method = 'Bluetooth')
        RETURN 
            d1.id AS from_device, 
            d2.id AS to_device, 
            length(path) AS path_length
        ORDER BY length(path) DESC
        LIMIT 1
        """
        result = session.run(query)
        return [
            {
                "from_device": record["from_device"],
                "to_device": record["to_device"],
                "path_length": record["path_length"]
            } for record in result
        ]

def devices_by_signal_strength():
   with driver.session() as session:
       query = """
        MATCH (d1:Device)-[r:Interaction]->(d2:Device)
        WHERE r.signal_strength_dbm	 > -60
        RETURN d1, d2, r.signal_strength_dbm
        """
       result = session.run(query).data()
       return result

def count_connected_devices(device_id):
    query = """
    MATCH (d:Device)-[:CONNECTED_TO]->(connected:Device)
    WHERE d.id = $device_id
    RETURN COUNT(connected) AS connected_count
    """
    with driver.session() as session:
        result = session.run(query, device_id=device_id)
        record = result.single()
        return record["connected_count"] if record else 0


def determine_direct_connection_between_two_devices(device_id_1, device_id_2):
    query = """
    MATCH (d1:Device)-[:CONNECTED_TO]->(d2:Device)
    WHERE d1.id = $device_id_1 AND d2.id = $device_id_2
    RETURN COUNT(d1) AS connection_count
    """
    with driver.session() as session:
        result = session.run(query, device_id_1=device_id_1, device_id_2=device_id_2)
        record = result.single()
        return record["connection_count"] > 0

def get_most_recent_interaction_repo(device_id):
   with driver.session() as session:
       query = f"""
        MATCH (d:Device)-[r:Interaction]->(:Device)
        WHERE d.id =  $device_id
        RETURN r.timestamp AS timestamp
        ORDER BY r.timestamp DESC
        LIMIT 1"""
       params = {"device_id": device_id}
       result = session.run(query, params)
       record = result.single()
       return record["timestamp"] if record else 0