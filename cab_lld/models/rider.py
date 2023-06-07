import uuid
from models.app_user import AppUser

class Rider(AppUser):
    
    def __init__(self, name=None, email=None, phone_number=None) -> None:
        super().__init__(name, email, phone_number)
        
        self.id = str(uuid.uuid4())
        
    def get_rider_id(self):
        return self.id
    