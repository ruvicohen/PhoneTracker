query_bluetooth_connections = """
        MATCH (d1:Device)
        MATCH (d2:Device)
        WHERE d1 <> d2
        MATCH path = (d1)-[r:Interaction*]->(d2)
        WHERE all(rel IN r WHERE rel.method = 'Bluetooth')
        RETURN 
            d1.id AS from_device, 
            d2.id AS to_device, 
            length(path) AS path_length
        ORDER BY length(path) DESC
        LIMIT 1
        """

query_devices_by_signal_strength = """
        MATCH (d1:Device)-[r:Interaction]->(d2:Device)
        WHERE r.signal_strength_dbm	 > -60
        RETURN d1, d2, r.signal_strength_dbm
        """

query_count_connected_devices = """
    MATCH (d:Device) <-[:Interaction]- (connected:Device)
    WHERE d.id = $device_id
    RETURN COUNT(connected) AS connected_count
    """

query_determine_direct_connection_between_two_devices = """
    MATCH (d1:Device)-[:Interaction]->(d2:Device)
    WHERE d1.id = $device_id_1 AND d2.id = $device_id_2
    RETURN COUNT(d1) AS connection_count
    """

query_most_recent_interaction_repo = f"""
        MATCH (d:Device)-[r:Interaction]->(:Device)
        WHERE d.id =  $device_id
        RETURN r.timestamp AS timestamp
        ORDER BY r.timestamp DESC
        LIMIT 1"""