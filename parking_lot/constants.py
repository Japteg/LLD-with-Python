from types import SimpleNamespace

PARKING_LOT_ID = 'PR1234'

VEHICLE_TYPES = SimpleNamespace(**{
    'BIKE': 'BIKE',
    'CAR': 'CAR',
    'TRUCK': 'TRUCK',
})

VALID_APIS = [
    'create_parking_lot',
    'park_vehicle',
    'unpark_vehicle',
]
