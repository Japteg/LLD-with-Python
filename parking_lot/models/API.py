from typing import List


class ApiCommand:
    """
    For eg: Input is => create_parking_lot <num_floors> <num_slots>
    Now this model is used to represent this input command
    """

    def __init__(self, api_name: str = None, api_parameters: List[str] = None):
        self.api_name = api_name
        self.api_parameters = api_parameters

    def set_api_name(self, endpoint: str):
        self.api_name = endpoint

    def set_api_parameters(self, parameters: List[str]):
        self.api_parameters = parameters

    def get_api_name(self) -> str:
        return self.api_name

    def get_api_parameters(self) -> List[str]:
        return self.api_parameters
