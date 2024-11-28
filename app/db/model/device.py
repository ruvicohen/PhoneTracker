from dataclasses import dataclass
from app.db.model.location import Location


@dataclass
class Device:
    id: str
    name: str
    brand: str
    model: str
    os: str
    latitude: float
    longitude: float
    altitude_meters: float
    accuracy_meters: float