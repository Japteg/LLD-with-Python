from typing import Dict
from parking_lot.models.parking_slot import Slot
from parking_lot.models.vehicle import Vehicle


class ParkingSlotService:

    def __init__(self):
        self.slots: Dict[str, Slot] = {}

    def get_slots(self) -> Dict[str, Slot]:
        return self.slots

    def create_parking_slot(self, floor_number: int, slot_number: int) -> Slot:
        parking_slot = Slot(floor_number, slot_number)
        self.slots[parking_slot.id] = parking_slot
        return parking_slot

    def park_vehicle(self, floor_number: int, slot_number: int, vehicle: Vehicle):
        slot_id = self.get_slot_id(floor_number, slot_number)
        if slot_id in self.slots.keys():
            parking_slot = self.slots[slot_id]
            parking_slot.set_parked_vehicle(vehicle)
        else:
            print(f'Parking slot does not exist: {floor_number}, {slot_number}')
            raise

    def unpark_vehicle(self, floor_number: int, slot_number: int):
        slot_id = self.get_slot_id(floor_number, slot_number)
        if slot_id in self.slots.keys():
            original_slot = self.slots[slot_id]
            # Re-Initialize slot
            self.slots[slot_id] = Slot(floor_number, slot_number)
            return original_slot
        else:
            print(f'Parking slot does not exist: {floor_number}, {slot_number}')
            raise

    @staticmethod
    def get_slot_id(floor_number, slot_number):
        return '_'.join([str(floor_number), str(slot_number)])
