from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.models.API import ApiCommand
from parking_lot.apis.api_interface import ApiInterface


class CreateParkingLotAPI(ApiInterface):

    API_NAME = 'create_parking_lot'

    def __init__(self, api_command: ApiCommand,
                 parking_lot_service: ParkingLotService):
        self.api_command = api_command
        self.parking_lot_service = parking_lot_service

    def execute(self):
        """
        Execute api call
        :return:
        """
        if not self.is_valid_api():
            raise ValueError
        num_floors = int(self.api_command.get_api_parameters()[0])
        num_slots = int(self.api_command.get_api_parameters()[1])
        self.parking_lot_service.create_parking_lot(num_floors, num_slots)
        print(f'Created parking lot with {num_floors} floors and {num_slots} '
              f'slots per floor')

    def is_valid_api(self):
        """
        Check if api command is valid
        :return:
        """
        try:
            int(self.api_command.get_api_parameters()[0])
            int(self.api_command.get_api_parameters()[0])
        except Exception as e:
            return False

        return self.api_command.get_api_name() == self.API_NAME and \
               len(self.api_command.get_api_parameters()) == 2
