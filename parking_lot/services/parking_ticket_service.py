from typing import Dict

from parking_lot.models.parking_ticket import ParkingTicket
from parking_lot.models.vehicle import Vehicle
from parking_lot.exceptions import InvalidTicketException


class ParkingTicketService:

    # Store all tickets
    TICKETS: Dict[str, ParkingTicket] = {}

    def __init__(self):
        pass

    def create_parking_ticket(self, floor: int, slot: int, vehicle: Vehicle) -> ParkingTicket:
        parking_ticket = ParkingTicket(floor, slot, vehicle)
        self.TICKETS[parking_ticket.ticket_id] = parking_ticket
        return parking_ticket

    def get_ticket(self, ticket_id: str) -> ParkingTicket:
        if ticket_id not in self.TICKETS.keys():
            raise InvalidTicketException
        return self.TICKETS[ticket_id]

    def invalidate_ticket(self, ticket_id: str):
        if ticket_id in self.TICKETS.keys():
            del self.TICKETS[ticket_id]
