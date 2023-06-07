import sys
import os
import traceback
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from parking_lot.services.parking_lot_service import ParkingLotService
from parking_lot.input_parser.file_mode_input import FileModeInput

try:
    parking_lot_service = ParkingLotService()
    input_parser = FileModeInput(parking_lot_service)
    input_parser.parse()
except Exception as e:
    traceback.print_exc()
    print(e)
