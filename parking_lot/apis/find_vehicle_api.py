from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.models.API import ApiCommand
from parking_lot.apis.api_interface import ApiInterface


class FindVehicleAPI(ApiInterface):

    API_NAME = 'find'

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
            registration_number = parameters[0]
            slots = self.parking_lot_service.get_all_slots().values()
            required_slot = filter(
                lambda slot:
                slot.get_parked_vehicle().get_registration_number() ==
                registration_number if slot.get_parked_vehicle() is not None else False,
                slots)
            required_slot = list(required_slot)
            required_slot = required_slot[0] if len(required_slot) > 0 else None
            if required_slot:
                floor_number = required_slot.get_floor_number()
                slot_number = required_slot.get_slot_number()
                print(f'Vehicle with registration number {registration_number} '
                      f'is parked on floor {floor_number} in slot {slot_number}')
            else:
                print(f'Vehicle with registration number {registration_number} not '
                      f'found')

        except Exception as e:
            pass

    def is_valid_api(self):
        """
        Check if api command is valid
        :return:
        """
        if len(self.api_command.get_api_parameters()) != 1:
            return False

        return True
