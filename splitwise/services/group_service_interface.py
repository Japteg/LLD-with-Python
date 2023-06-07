import abc


class GroupServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_group(self, id, name, members):
        pass
