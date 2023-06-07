from splitwise.services.group_service_interface import GroupServiceInterface
from splitwise.models.group import Group


class GroupService(GroupServiceInterface):

    GROUP_DETAILS = {}

    def add_group(self, id, name, members):
        group = Group()
        group.set_id(id)
        group.set_name(name)
        group.set_members(members)
        self.__class__.GROUP_DETAILS[id] = group
        return group
