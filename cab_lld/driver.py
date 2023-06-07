from managers.cab_manager import CabManager
from managers.rider_manager import RiderManager
from managers.trip_manager import TripManager

from services.cab_service import CabService
from services.rider_service import RiderService

cab_manager = CabManager()
rider_manager = RiderManager()
trip_manager = TripManager(cab_manager, rider_manager)

cab_service = CabService(cab_manager, trip_manager)
rider_service = RiderService(rider_manager, trip_manager)

# API calls
cab1 = cab_service.register_cab()
cab2 = cab_service.register_cab()
cab3 = cab_service.register_cab()
cab4 = cab_service.register_cab()
print(cab_service.get_cabs())

rider1 = rider_service.register_rider('Japteg')
rider2 = rider_service.register_rider('Jasveen')
rider3 = rider_service.register_rider('Harjeet')
rider4 = rider_service.register_rider('Maninder')

rider_service.book_cab(rider1.get_rider_id(), 0, 15)
rider_service.book_cab(rider2.get_rider_id(), 5, 34)
rider_service.book_cab(rider3.get_rider_id(), 12, 19)
rider_service.book_cab(rider4.get_rider_id(), 32, 100)

cab_service.end_trip(cab1.get_cab_id())
cab_service.end_trip(cab4.get_cab_id())

print(cab_manager.get_available_cabs())

cab_service.end_trip(cab2.get_cab_id())
cab_service.end_trip(cab3.get_cab_id())

print(rider_service.get_trip_history(rider1))

