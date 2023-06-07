from parking_lot.models.vehicle import Vehicle


class VehicleService:
    def __init__(self):
        pass

    @staticmethod
    def create_vehicle_object(vehicle_type, reg_number, color):
        return Vehicle(vehicle_type, reg_number, color)
