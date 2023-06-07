from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.models.API import ApiCommand
from parking_lot.apis.api_interface import ApiInterface


class DisplayAPI(ApiInterface):

    API_NAME = 'display'

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
            parameters = self.api_command.get_api_parameters()
            query = parameters[0]
            vehicle_type = parameters[1]
            if query == 'free_count':
                DisplayFreeCountAPI(self.parking_lot_service, vehicle_type).execute()
            elif query == 'occupied_count':
                DisplayOccupiedCountAPI(self.parking_lot_service, vehicle_type).execute()
            else:
                print('Invalid argument for Display API.')
        except Exception as e:
            pass

    def is_valid_api(self):
        """
        Check if api command is valid
        :return:
        """
        if len(self.api_command.get_api_parameters()) != 2:
            return False

        if self.api_command.get_api_parameters()[0] not in \
                ['free_count', 'occupied_count']:
            return False

        return True


class DisplayFreeCountAPI:
    """
    Displays number of free slots for particular vehicle type
    """

    def __init__(self, parking_lot_service: ParkingLotService, vehicle_type):
        self.parking_lot_service = parking_lot_service
        self.vehicle_type = vehicle_type

    def execute(self):
        all_available_slots = self.parking_lot_service.parking_strategy.available_slots
        vehicle_available_slots = len(all_available_slots.get(self.vehicle_type, []))
        print(f'No. of free slots for {self.vehicle_type}: {vehicle_available_slots}')


class DisplayOccupiedCountAPI:
    """
    Displays number of occupied slots for particular vehicle type
    """

    def __init__(self, parking_lot_service: ParkingLotService, vehicle_type):
        self.parking_lot_service = parking_lot_service
        self.vehicle_type = vehicle_type

    def execute(self):
        all_available_slots = self.parking_lot_service.parking_strategy.available_slots
        vehicle_available_slots = len(all_available_slots.get(self.vehicle_type, []))
        vehicle_total_slots = self.parking_lot_service.total_slot_count_each_vehicle.get(
            self.vehicle_type, 0)
        vehicle_occupied_slots = vehicle_total_slots - vehicle_available_slots
        if vehicle_occupied_slots < 0:
            print('Unexpected state. Please contact tech support')
            return

        print(f'No. of occupied slots for {self.vehicle_type}: {vehicle_occupied_slots}')
