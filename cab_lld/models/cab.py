import uuid
from models.location import Location
from models.trip import Trip


class Cab:
    def __init__(self, driver, location) -> None:
        self.cab_id = str(uuid.uuid4())
        self.driver = driver # 1:1 mapping
        self.current_location:Location = location
        self.is_available = True
        self.current_trip = None
        
    def get_cab_id(self):
        return self.cab_id
    
    def get_cab_loaction(self):
        return self.current_location
    
    def set_cab_loaction(self, location:Location):
        self.current_location = location
        
    def get_cab_availability(self):
        return self.is_available
    
    def set_cab_availability(self, is_available: bool):
        self.is_available = is_available
        
    def get_current_trip(self) -> Trip:
        return self.current_trip
    
    def set_current_trip(self, trip):
        self.current_trip = trip
        