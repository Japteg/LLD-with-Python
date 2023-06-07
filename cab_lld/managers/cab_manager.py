from typing import Dict
from models.cab import Cab
from models.location import Location
from models.driver import Driver


class CabManager:
    Cabs: Dict[str, Cab] = {}
    
    def __init__(self) -> None:
        pass
    
    def add_cab(self, driver=None, x_loc=0, y_loc=0):
        cab_location = Location(x_loc, y_loc)
        new_cab = Cab(driver, cab_location)
        self.__class__.Cabs[new_cab.get_cab_id()] = new_cab
        return new_cab
        
    def update_cab_loaction(self, cab_id, x_loc=0, y_loc=0):
        cab = self.Cabs[cab_id]
        cab.set_cab_loaction(Location(x_loc, y_loc))
        return cab
    
    def update_cab_availability(self, cab_id, availability:bool):
        cab = self.Cabs[cab_id]
        cab.set_cab_availability(availability)
    
    def get_cab(self, cab_id):
        return self.Cabs[cab_id]
    
    def get_available_cabs(self):
        return list(filter(lambda x: x.is_available == True, list(self.Cabs.values())))
        
            