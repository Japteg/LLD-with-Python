import uuid


class Vehicle:
    def __init__(self, vehicle_type=None, reg_number=None, color=None):
        self.id = uuid.uuid4()
        self.type = vehicle_type
        self.registration_number = reg_number
        self.color = color

    def set_type(self, vehicle_type):
        self.type = vehicle_type

    def set_registration_number(self, reg_number):
        self.registration_number = reg_number

    def set_color(self, color):
        self.color = color

    def get_type(self):
        return self.type

    def get_registration_number(self):
        return self.registration_number

    def get_color(self):
        return self.color
