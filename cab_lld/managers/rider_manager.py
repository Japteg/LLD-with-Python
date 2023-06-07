from typing import Dict
from models.rider import Rider


class RiderManager:
    
    Riders: Dict[str, Rider] = {}
    
    def __init__(self) -> None:
        pass    
    
    def add_rider(self, Name, email=None, phone=None):
        new_rider = Rider(Name, email, phone)
        self.__class__.Riders[new_rider.get_rider_id()] = new_rider
        return new_rider
    
    def get_rider(self, rider_id):
        return self.Riders[rider_id]