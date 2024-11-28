from app.repository.crud_node import create_node, create_relationship, delete_all_nodes

create_device = create_node("Device")

add_interaction = create_relationship("Interaction", "Device", "Device")

def delete_devices():
    return delete_all_nodes("Device")