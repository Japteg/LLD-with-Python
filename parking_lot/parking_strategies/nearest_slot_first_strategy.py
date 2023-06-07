from sortedcontainers import SortedList
from typing import Dict

from parking_lot.exceptions import ParkingLotFullException


class NearestSlotFirstStrategy:

    def __init__(self):
        # Will be used to store available slots for each floor based on vehicle type
        self.available_slots: Dict[str, SortedList[int]] = {}

    def add_slot(self, floor_number: int, slot_number: int, vehicle_type: str):
        """
        Make slot available
        """
        if vehicle_type not in self.available_slots.keys():
            self.available_slots[vehicle_type] = SortedList([[floor_number, slot_number]])
        else:
            self.available_slots[vehicle_type].add([floor_number, slot_number])

    def remove_slot(self, floor_number: int, slot_number: int):
        """
        Removes slot from available slots
        """
        for key in self.available_slots.keys():
            for row in self.available_slots[key]:
                if row[0] == floor_number and row[1] == slot_number:
                    self.available_slots[key].discard([floor_number, slot_number])

    def next_slot(self, vehicle_type):
        """
        :return: next appropriate floor_number and slot number according to strategy
        """
        if vehicle_type in self.available_slots.keys() and \
                len(self.available_slots[vehicle_type]) > 0:
            return self.available_slots[vehicle_type][0]
        else:
            raise ParkingLotFullException(vehicle_type)
