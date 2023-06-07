from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.models.API import ApiCommand
from parking_lot.apis.api_interface import ApiInterface
from parking_lot.exceptions import InvalidTicketException


class UnparkVehicleAPI(ApiInterface):

    API_NAME = 'unpark_vehicle'

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
            ticket_id = self.api_command.get_api_parameters()[0]
            parking_ticket = self.parking_lot_service.unpark_vehicle(ticket_id)
            vehicle = parking_ticket.get_vehicle()
            print(f'Unparked vehicle with Registration Number: '
                  f'{vehicle.get_registration_number()} and Color: {vehicle.get_color()}')
        except InvalidTicketException as e:
            print('Invalid Ticket')

    def is_valid_api(self):
        """
        Check if api command is valid
        :return:
        """
        if len(self.api_command.get_api_parameters()) != 1:
            return False

        return True
