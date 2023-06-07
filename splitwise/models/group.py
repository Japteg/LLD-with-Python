class Group:
    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.members = []

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_members(self, members):
        self.members = members

    def get_members(self):
        return self.members
