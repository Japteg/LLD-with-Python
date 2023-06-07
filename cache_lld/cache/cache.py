from .cache_interface import CacheInterface
from .policies.eviction_policy_interface import EvictionPolicyInterface
from .storage.storage_interface import StorageInterface
from .exceptions.exceptions import StorageFullException, NotFoundException


class Cache(CacheInterface):

    def __init__(self, eviction_policy: EvictionPolicyInterface,
                 storage: StorageInterface):
        self.eviction_policy = eviction_policy
        self.storage = storage

    def put(self, key, value):
        try:
            self.storage.add(key, value)
            self.eviction_policy.key_accessed(key)
            print(f'Item added in cache: {key}')
        except StorageFullException:
            print("Storage is full.")
            evict_key = self.eviction_policy.evict()
            self.storage.remove(evict_key)
            print(f"******Removed item {evict_key} from cache*******")
            self.put(key, value)

    def get(self, key):
        value = None
        try:
            value = self.storage.get(key)
            self.eviction_policy.key_accessed(key)
            print(f"Getting item {key} from cache: {value}")
        except NotFoundException:
            print(f'Key not present in cache: {key}')

        return value
