from eviction_policies.eviction_policy import EvictionPolicy
from eviction_policies.cache import Cache
from eviction_policies.lru import LRUPolicy
from eviction_policies.fifo import FIFOPolicy
from eviction_policies.lfu import LFUPolicy
from eviction_policies.lifo import LIFOPolicy
from eviction_policies.mru import MRUPolicy

# Create a cache with LRU policy
cache = Cache(capacity=3, eviction_policy=LRUPolicy())

# Add items
cache.put("key1", "value1")
cache.put("key2", "value2")
cache.put("key3", "value3")

# Access items
value = cache.get("key1")  # Returns "value1"

# Adding a fourth item will evict the least recently used item
cache.put("key4", "value4")