class GroupController:
    def __init__(self, group_service):
        self.group_service = group_service

    def add_group(self, id, name, members):
        return self.group_service.add_group(id, name, members)
