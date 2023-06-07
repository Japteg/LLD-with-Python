from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.models.API import ApiCommand
from parking_lot.apis.api_interface import ApiInterface
from parking_lot.constants import VEHICLE_TYPES


class ParkVehicleAPI(ApiInterface):

    API_NAME = 'park_vehicle'

    def __init__(self, api_command: ApiCommand,
                 parking_lot_service: ParkingLotService):
        self.api_command = api_command
        self.parking_lot_service = parking_lot_service

    def execute(self):
        """
        Execute api call
        :return:
        """
        try:
            vehicle_type = self.api_command.get_api_parameters()[0]
            registration_numner = self.api_command.get_api_parameters()[1]
            color = self.api_command.get_api_parameters()[2]
            ticket = self.parking_lot_service.park_vehicle(
                vehicle_type, registration_numner, color)
            print(f'Parked vehicle. Ticket ID: {ticket.ticket_id}')
        except Exception as e:
            pass

    def is_valid_api(self):
        """
        Check if api command is valid
        :return:
        """
        if len(self.api_command.get_api_parameters()) != 3:
            return False

        if self.api_command.get_api_parameters()[0] not in VEHICLE_TYPES.__dict__:
            return False

        return True
