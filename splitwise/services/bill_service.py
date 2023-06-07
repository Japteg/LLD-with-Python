from splitwise.services.bill_service_interface import BillServiceInterface
from splitwise.models.bill import Bill


class BillService(BillServiceInterface):

    BILL_DETAILS = {}

    def add_bill(self, id, group_id, amount, contribution, paid_by):
        bill = Bill()
        bill.set_id(id)
        bill.set_group_id(group_id)
        bill.set_amount(amount)
        bill.set_contribution(contribution)
        bill.set_paid_by(paid_by)
        self.__class__.BILL_DETAILS[id] = bill
        return bill
