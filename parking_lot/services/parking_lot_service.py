from typing import Dict
from parking_lot.models.parking_lot import ParkingLot
from parking_lot.models.parking_ticket import ParkingTicket
from parking_lot.parking_strategies.nearest_slot_first_strategy import \
    NearestSlotFirstStrategy
from parking_lot.services.parking_slot_service import ParkingSlotService
from parking_lot.services.parking_ticket_service import ParkingTicketService
from parking_lot.services.vehicle_service import VehicleService
from parking_lot.utils import parking_lot_exists
from parking_lot.exceptions import ParkingLotFullException


class ParkingLotService:
    def __init__(self, parking_lot: ParkingLot = None):
        self.parking_lot = parking_lot
        self.parking_slot_service = ParkingSlotService(parking_lot)
        self.parking_strategy = NearestSlotFirstStrategy()
        self.total_slot_count_each_vehicle: Dict[str, int] = {}

    def create_parking_lot(self, num_floors, num_slots):
        # We are assuming only one parking lot, hence this check
        if self.parking_lot is not None:
            print("Parking lot already exists!!")
            raise ValueError
        self.parking_lot = ParkingLot(num_floors, num_slots)
        for floor_number in range(1, num_floors+1):
            for slot_number in range(1, num_slots + 1):
                slot = self.parking_slot_service.create_parking_slot(floor_number,
                                                                     slot_number)
                self.parking_strategy.add_slot(floor_number, slot_number,
                                               slot.get_slot_type())
                self.total_slot_count_each_vehicle[slot.get_slot_type()] = \
                    self.total_slot_count_each_vehicle.get(slot.get_slot_type(), 0) + 1

    @parking_lot_exists
    def park_vehicle(self, vehicle_type, reg_number, color) -> ParkingTicket:
        try:
            floor_number, slot_number = self.parking_strategy.next_slot(vehicle_type)
            vehicle = VehicleService().create_vehicle_object(vehicle_type, reg_number,
                                                             color)
            ticket = ParkingTicketService().create_parking_ticket(
                floor_number, slot_number, vehicle)
            # Park vehicle at given floor and slot
            self.parking_slot_service.park_vehicle(floor_number, slot_number, vehicle)
            self.parking_strategy.remove_slot(floor_number, slot_number)
            return ticket
        except ParkingLotFullException as e:
            print(e)

    @parking_lot_exists
    def unpark_vehicle(self, ticket_id: str) -> ParkingTicket:
        parking_ticket = ParkingTicketService().get_ticket(ticket_id)
        floor_number = parking_ticket.get_floor()
        slot_number = parking_ticket.get_slot()
        free_slot = \
            self.parking_slot_service.unpark_vehicle(floor_number, slot_number)
        # This ticket is no longer valid
        ParkingTicketService().invalidate_ticket(ticket_id)
        # Make slot available
        self.parking_strategy.add_slot(floor_number, slot_number,
                                       free_slot.get_slot_type())
        return parking_ticket

    @parking_lot_exists
    def get_all_slots(self):
        return self.parking_slot_service.get_slots()
