# In-Memory Cache Library

This is an extensible in-memory cache library that supports multiple eviction policies. It allows the user to easily integrate caching functionality into their applications.

## Features

- Thread-safe cache implementation
- Support for the following eviction policies:
  - **FIFO (First-In-First-Out)**: Evicts the oldest items first
  - **LIFO (Last-In-First-Out)**: Evicts the newest items first
  - **LRU (Least Recently Used)**: Evicts the least recently used items
  - **MRU (Most Recently Used)**: Evicts the most recently used items
  - **LFU (Least Frequently Used)**: Evicts the least frequently used items
- Ability to add custom eviction policies
- Functionalities are verified using unit testing.

## Installation

To use the cache library, simply copy the `cache_lib` directory into your project.

## Usage

Here's an example of how to use the cache:

```python
from eviction_policies.cache import Cache
from eviction_policies.lru import LRUPolicy

"""
 When creating a Cache instance specify the desired eviction policy.
 E.g.: Create a cache with LRU eviction policy and capacity of 100 items
"""
cache = Cache(capacity=100, eviction_policy=LRUPolicy())

# Add items to the cache
cache.put("key1", "value1")
cache.put("key2", "value2")

# Retrieve items from the cache
value = cache.get("key1")  # Returns "value1"
value = cache.get("key2")  # Returns "value2"

# Remove an item from the cache
cache.remove("key1")

# Clear the entire cache
cache.clear()
```

## Adding Custom Eviction Policies

- To add a custom eviction policy, create a new class that inherits from the EvictionPolicy base class and implements the required methods. Then, you can use the custom policy when creating a new cache instance.

```python
from eviction_policies.cache import Cache
from eviction_policies.eviction_policy import EvictionPolicy

class MyCustomPolicy(EvictionPolicy):
     """ Implement the required methods
     such as on_get, on_put, evict, etc.
     """

cache = Cache(capacity=100, eviction_policy=MyCustomPolicy())
```

## Testing
- The library also includes a unit test suite that ensures the correct behavior of the cache and eviction policies, including thread safety. You can run the tests using the following command:

```bash
python -m unittest discover -s tests -p "test_*.py"
```
