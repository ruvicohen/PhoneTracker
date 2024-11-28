from app.repository.crud_node import create_node, create_relationship

create_device = create_node("Device")

add_interaction = create_relationship("Device", "Device")