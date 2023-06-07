from cache_lld.cache.cache import Cache
from cache_lld.cache.storage.dict_storage import DictStorage
from cache_lld.cache.policies.LRU_eviction_policy import LRUEvictionPolicy


class CacheFactory:

    """
    Factory design pattern
    cache object is only created through cache factory and not directly initialized
    by importing the cache class.

    Cache factory is the single point of creation for different types of cache.
    You can further extend this code to incorporate different combination
    of eviction policy and storage
    """

    @staticmethod
    def default_cache(capacity: int) -> Cache:
        return Cache(LRUEvictionPolicy(), DictStorage(capacity))
