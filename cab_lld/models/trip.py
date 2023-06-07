from enum import Enum

class TripStatus(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2

class Trip:
    def __init__(self, from_location, to_location, rider, cab, fare) -> None:
        self.from_loaction = from_location
        self.to_loaction = to_location
        self.rider = rider
        self.cab = cab
        self.fare = fare
        self.status = None
        
    def start_trip(self):
        self.status = TripStatus.IN_PROGRESS
        
    def end_trip(self):
        self.status = TripStatus.COMPLETED
    