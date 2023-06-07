import abc


class ApiInterface(metaclass=abc.ABCMeta):

    """
    API interface
    These functions must be implemented by all APIs
    """

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def is_valid_api(self):
        pass
