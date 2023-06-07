import abc


class BillServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_bill(self, id, group_id, amount, contribution, paid_by):
        pass
