class User:
    def __init__(self) -> None:
        self.id = None
        self.name = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
