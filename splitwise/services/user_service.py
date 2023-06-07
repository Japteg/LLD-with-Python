from splitwise.services.user_service_interface import UserServiceInterface
from splitwise.models.user import User


class UserService(UserServiceInterface):

    USER_DETAILS = {}

    def add_user(self, id, name):
        user = User()
        user.set_id(id)
        user.set_name(name)
        self.__class__.USER_DETAILS[id] = user
        return user
