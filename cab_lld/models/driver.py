from models.app_user import AppUser

class Driver(AppUser):
    
    def __init__(self, name, email, phone_number) -> None:
        super().__init__(name, email, phone_number)
        self.rating = None
        
    def set_rating(self, rating):
        self.rating = rating
        
    def get_rating(self):
        return self.rating