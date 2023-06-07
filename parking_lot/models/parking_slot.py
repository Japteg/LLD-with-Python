from parking_lot.constants import VEHICLE_TYPES
from parking_lot.models.vehicle import Vehicle


class Slot:

    def __init__(self, floor_number: int, slot_number: int,
                 parked_vehicle: Vehicle = None):
        self.id = '_'.join([str(floor_number), str(slot_number)])
        self.floor_number = floor_number
        self.slot_number = slot_number
        self.parked_vehicle = parked_vehicle
        self.slot_type = None
        # Initialize slot type
        self.update_slot_type()

    def set_slot_number(self, slot_number):
        self.slot_number = slot_number
        self.update_slot_type()

    def set_parked_vehicle(self, vehicle: Vehicle):
        self.parked_vehicle = vehicle

    def get_slot_id(self):
        return self.id

    def get_slot_number(self):
        return self.slot_number

    def get_floor_number(self):
        return self.floor_number

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle

    def get_slot_type(self):
        return self.slot_type

    def update_slot_type(self):
        """
        Slot 1 is for truck
        slot 2 and 3 is for bike
        rest are for cars
        :return:
        """
        if self.slot_number == 1:
            self.slot_type = VEHICLE_TYPES.TRUCK
        elif self.slot_number <= 3:
            self.slot_type = VEHICLE_TYPES.BIKE
        else:
            self.slot_type = VEHICLE_TYPES.CAR
