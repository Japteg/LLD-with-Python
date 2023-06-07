from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.input_parser.input_parser_base import InputParserBase
from parking_lot.models.API import ApiCommand


class FileModeInput(InputParserBase):
    """
    This class is inheriting from InputParserBase class
    This is done to avoid re-implementation of process_api_command function
    for all different types of input mode
    """
    def __init__(self, parking_lot_service: ParkingLotService,
                 input_file_path: str = 'sample_input.txt'):
        self.parking_lot_service = ParkingLotService
        self.file_path = input_file_path
        super().__init__(parking_lot_service)

    def parse(self):
        with open(self.file_path, 'r') as input_file:
            for row in input_file:
                row = row.strip(' ').rstrip('\n').split(' ')
                command_name = row[0]
                command_parameters = row[1:]
                api_command = ApiCommand(command_name, command_parameters)
                self.process_api_command(api_command)
