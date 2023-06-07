import abc


class CacheInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def put(self, key, value):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass
