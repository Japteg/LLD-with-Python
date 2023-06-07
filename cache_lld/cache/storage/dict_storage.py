from cache_lld.cache.exceptions.exceptions import StorageFullException, NotFoundException
from .storage_interface import StorageInterface


class DictStorage(StorageInterface):

    def __init__(self, capacity):
        self.storage = {}
        self.capacity = capacity

    def add(self, key: any, value: any) -> None:
        if self.is_storage_full():
            raise StorageFullException()

        self.storage[key] = value

    def remove(self, key: any) -> None:
        if key not in self.storage.keys():
            raise NotFoundException

        del self.storage[key]

    def get(self, key: any) -> any:
        if key not in self.storage.keys():
            raise NotFoundException

        return self.storage[key]

    def is_storage_full(self) -> bool:
        return len(self.storage) >= self.capacity
