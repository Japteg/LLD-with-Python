class BillController:
    def __init__(self, bill_service):
        self.bill_service = bill_service

    def add_bill(self, id, group_id, amount, contribution, paid_by):
        return self.bill_service.add_bill(id, group_id, amount, contribution, paid_by)

    def get_user_balance(self, user_id):
        balance = 0
        for bill_id in self.bill_service.BILL_DETAILS:
            bill = self.bill_service.BILL_DETAILS.get(bill_id)
            contribution = bill.get_contribution()
            paid_by = bill.get_paid_by()
            if user_id in contribution:
                balance -= contribution.get(user_id, 0)
            if user_id in paid_by:
                balance += paid_by.get(user_id, 0)

        return balance
