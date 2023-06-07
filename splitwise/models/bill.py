class Bill:
    def __init__(self) -> None:
        self.id = None
        self.group_id = None
        self.amount = None
        self.contribution = {}
        self.paid_by = {}

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_group_id(self, group_id):
        self.group_id = group_id

    def get_group_id(self):
        return self.group_id

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_contribution(self, contribution):
        self.contribution = contribution

    def get_contribution(self):
        return self.contribution

    def set_paid_by(self, paid_by):
        self.paid_by = paid_by

    def get_paid_by(self):
        return self.paid_by
