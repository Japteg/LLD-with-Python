from typing import Dict, List
from managers.cab_manager import CabManager
from managers.rider_manager import RiderManager
from models.cab import Cab
from models.rider import Rider
from models.trip import Trip


class TripManager:
    
    Trips : Dict[str, List[Rider]] = {}
    
    def __init__(self, cab_manager, rider_manager) -> None:
        self.cab_manager:CabManager = cab_manager
        self.rider_manager:RiderManager = rider_manager
        
    def create_trip(self, rider, from_point, to_point):
        fare = 100 # self.fare_strategy.get_fare(from_point, to_point)
        available_cabs = self.cab_manager.get_available_cabs()
        selected_cab = available_cabs[0] # self.cab_selection_strategy.match_cab(rider, available_cabs)
        new_trip = Trip(from_point, to_point, rider, selected_cab, fare)
        new_trip.start_trip()
        self.cab_manager.update_cab_availability(selected_cab.get_cab_id(), False)
        selected_cab.set_current_trip(new_trip)
        
        self.Trips[rider.get_rider_id()] = self.Trips.get(rider.get_rider_id(), []) + [new_trip]
        return new_trip
        
    def get_trip_history(self, rider):
        return self.Trips[rider.get_rider_id()]
    
    def end_trip(self, cab:Cab):
        cab.get_current_trip().end_trip()
        cab.set_cab_availability(True)
        