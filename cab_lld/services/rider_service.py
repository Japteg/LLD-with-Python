from managers.rider_manager import RiderManager
from managers.trip_manager import TripManager

class RiderService:
    def __init__(self, rider_manager: RiderManager, trip_manager: TripManager) -> None:
        self.rider_manager = rider_manager
        self.trip_manager = trip_manager
    
    # POST : /rider
    def register_rider(self, name):
        new_rider = self.rider_manager.add_rider(name)
        print(f'Rigestered new rider: {new_rider.name}')
        return new_rider
        
    # POST: /rider/<rider_id>/book_cab
    def book_cab(self, rider_id, from_point, to_point):
        rider = self.rider_manager.get_rider(rider_id)
        self.trip_manager.create_trip(rider, from_point, to_point)
        
    # GET: /rider/<rider_id>/history
    def get_trip_history(self, rider):
        return self.trip_manager.get_trip_history(rider)
        