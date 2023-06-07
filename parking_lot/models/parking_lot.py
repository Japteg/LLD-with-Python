from typing import Dict
from parking_lot.utils import Singleton
from parking_lot.models.parking_slot import Slot
from parking_lot.models.vehicle import Vehicle


class ParkingLot(metaclass=Singleton):

    PARKING_LOT_ID = 'PR101'

    def __init__(self, num_floors: int = 2, num_slots: int = 20):
        self.num_floors = num_floors
        self.num_slots = num_slots
        # # Store all slots
        # self.slots: Dict[str, Slot] = {}

    # """
    # utility functions to manage slots
    # """
    # def get_slots(self) -> Dict[str, Slot]:
    #     return self.slots
    #
    # def get_slot(self, slot_id: str) -> Slot:
    #     if slot_id not in self.slots.keys():
    #         raise
    #
    #     return self.slots.get(slot_id)
    #
    # def add_slot(self, slot_id: str, parking_slot: Slot):
    #     self.slots[slot_id] = parking_slot
    #
    # def park(self, slot_id: str, vehicle: Vehicle):
    #     if slot_id in self.slots.keys():
    #         parking_slot = self.slots[slot_id]
    #         parking_slot.set_parked_vehicle(vehicle)
    #     else:
    #         print(f'Parking slot with id {slot_id} does not exist.')
    #         raise
    #
    # def unpark(self, slot_id: str):
    #     if slot_id in self.slots.keys():
    #         original_slot = self.slots[slot_id]
    #         # Re-Initialize slot
    #         floor_number = original_slot.get_floor_number()
    #         slot_number = original_slot.get_slot_number()
    #         self.slots[slot_id] = Slot(floor_number, slot_number)
    #         return original_slot
    #     else:
    #         print(f'Parking slot with id {slot_id} does not exist.')
    #         raise
