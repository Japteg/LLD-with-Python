class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def add_user(self, id, name):
        return self.user_service.add_user(id, name)
