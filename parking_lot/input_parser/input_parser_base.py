from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.apis.api_factory import ApiFactory
from parking_lot.models.API import ApiCommand
from parking_lot.exceptions import InvalidApiException


class InputParserBase:
    def __init__(self, parking_lot_service: ParkingLotService):
        self.parking_lot_service = parking_lot_service

    def process_api_command(self, api_command: ApiCommand):
        """
        Process API
        :param api_command:
        :return:
        """
        api_executor = ApiFactory(api_command, self.parking_lot_service).\
            get_api_executor()
        if api_executor.is_valid_api():
            api_executor.execute()
        else:
            raise InvalidApiException(api_command.get_api_name())
