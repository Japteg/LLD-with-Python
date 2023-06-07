from managers.cab_manager import CabManager
from managers.rider_manager import RiderManager
from managers.trip_manager import TripManager

class CabService:
    def __init__(self, cab_manager:CabManager, trip_manager: TripManager) -> None:
        self.cab_manager = cab_manager
        self.trip_manager = trip_manager
    
    # POST : /cab
    def register_cab(self):
        new_cab = self.cab_manager.add_cab()
        print(f'Rigestered new cab: {new_cab.get_cab_id()}')
        return new_cab
        
    # PUT: /cab/<cab_id>/availability
    def update_cab_availablity(self, cab_id):
        self.cab_manager.update_cab_availability(cab_id)
        
    # PUT: /cab/<cab_id>/location
    def update_car_location(self, cab_id, x_loc, y_loc):
        self.cab_manager.update_cab_loaction(cab_id, x_loc, y_loc)
        
    # POST: /cab/<cab_id>/end_trip
    def end_trip(self, cab_id):
        cab = self.cab_manager.get_cab(cab_id)
        self.trip_manager.end_trip(cab)
        print(f'Trip ended for cab id {cab_id}')
        
    # GET: /cabs
    def get_cabs(self):
        return self.cab_manager.get_available_cabs()
        