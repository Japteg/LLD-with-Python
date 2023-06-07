# import uuid
# from typing import Dict
# from parking_lot.models.parking_slot import Slot
#
#
# class ParkingFloor:
#     def __init__(self, floor_number=None, num_slots=100):
#         self.id = uuid.uuid4()
#         self.num_slots = num_slots  # Each floor can have this many slots at max
#         self.floor_number = floor_number
#         self.slots: Dict[int, Slot] = {}  # Map of slot number and slot object
#
#     def set_floor_number(self, floor_number: int):
#         self.floor_number = floor_number
#
#     def set_slots(self, slots: Dict[int, Slot]):
#         if len(slots) > self.num_slots:
#             raise ValueError
#         self.slots = slots
#
#     def get_floor_number(self) -> int:
#         return self.floor_number
#
#     def get_slots(self) -> Dict[int, Slot]:
#         return self.slots
