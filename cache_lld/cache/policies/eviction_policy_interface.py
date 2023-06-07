import abc

'''
***Eviction Policy Interface***
There can be many different types of eviction policy, for eg: LRU, LFU, FIFO etc
All implementations of eviction policy should inherit from this base interface
This will ensure consistency and maintainability of code base
'''


class EvictionPolicyInterface(metaclass=abc.ABCMeta):

    def key_accessed(self, key: any) -> None:
        pass

    def evict(self) -> None:
        pass

