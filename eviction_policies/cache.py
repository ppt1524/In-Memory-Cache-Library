from threading import Lock
from eviction_policies.eviction_policy import EvictionPolicy
from typing import Generic, TypeVar

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class Cache(Generic[KT, VT]):
    """Thread-safe in-memory cache with configurable eviction policy."""
    
    def __init__(self, capacity: int, eviction_policy: EvictionPolicy[KT]):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.capacity = capacity
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.lock = Lock()
    
    def get(self, key: KT) -> VT | None:
        """
        Retrieve an item from the cache.
        Returns None if the key doesn't exist.
        """
        with self.lock:
            if key in self.cache:
                self.eviction_policy.on_get(key)
                return self.cache[key]
            return None
    
    def put(self, key: KT, value: VT) -> None:
        """Add an item to the cache."""
        with self.lock:
            if key not in self.cache and len(self.cache) >= self.capacity:
                evicted_key = self.eviction_policy.evict()
                del self.cache[evicted_key]
            
            self.cache[key] = value
            self.eviction_policy.on_put(key)
    
    def remove(self, key: KT) -> None:
        """Remove an item from the cache."""
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        with self.lock:
            self.cache.clear()
            self.eviction_policy = type(self.eviction_policy)()
    
    def size(self) -> int:
        """Return the current number of items in the cache."""
        with self.lock:
            return len(self.cache)
