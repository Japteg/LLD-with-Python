from parking_lot.models.API import ApiCommand
from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.apis.api_interface import ApiInterface
from parking_lot.apis.create_parking_lot_api import CreateParkingLotAPI
from parking_lot.apis.park_vehicle_api import ParkVehicleAPI
from parking_lot.apis.unpark_vehicle_api import UnparkVehicleAPI
from parking_lot.apis.display_api import DisplayAPI
from parking_lot.apis.find_vehicle_api import FindVehicleAPI
from parking_lot.exceptions import InvalidApiException


class ApiFactory:
    """
    ApiFactory takes an api command
    Based on api command, it returns appropriate api object
    ** Factory design pattern **
    """

    API_EXECUTOR_MAP = {
        'create_parking_lot': CreateParkingLotAPI,
        'park_vehicle': ParkVehicleAPI,
        'unpark_vehicle': UnparkVehicleAPI,
        'display': DisplayAPI,
        'find': FindVehicleAPI,
    }

    def __init__(self, api_command: ApiCommand, parking_lot_service: ParkingLotService):
        self.api_command = api_command
        self.parking_lot_service = parking_lot_service

    def get_api_executor(self) -> ApiInterface:
        if self.api_command.get_api_name() not in self.API_EXECUTOR_MAP.keys():
            raise InvalidApiException(self.api_command.get_api_name())

        return self.API_EXECUTOR_MAP[self.api_command.get_api_name()](
            self.api_command, self.parking_lot_service)
