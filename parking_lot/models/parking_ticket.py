from parking_lot.constants import PARKING_LOT_ID
from parking_lot.models.vehicle import Vehicle


class ParkingTicket:

    def __init__(self, floor: int, slot: int, vehicle: Vehicle = None):
        self.ticket_id = None
        self.floor = floor
        self.slot = slot
        self.vehicle = vehicle
        # Initialize ticket
        self.update_ticket()

    def set_floor(self, floor):
        self.floor = floor
        self.update_ticket()

    def set_slot(self, slot):
        self.slot = slot
        self.update_ticket()

    def set_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def get_floor(self):
        return self.floor

    def get_slot(self):
        return self.slot

    def get_vehicle(self) -> Vehicle:
        return self.vehicle

    def get_ticket_id(self):
        return self.ticket_id

    def update_ticket(self):
        self.ticket_id = PARKING_LOT_ID + '_' + str(self.floor) + '_' + \
                         str(self.slot)
