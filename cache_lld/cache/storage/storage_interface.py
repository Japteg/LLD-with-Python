import abc

'''
***Storage Interface***
Since storage can be implemented using different data structures,
we have defined an interface which should be implemented by all different types of
storage in order to maintain consistency and maintainability of code base
'''


class StorageInterface(metaclass=abc.ABCMeta):

    def add(self, key: any, value: any) -> None:
        pass

    def remove(self, key: any) -> None:
        pass

    def get(self, key: any) -> any:
        pass
