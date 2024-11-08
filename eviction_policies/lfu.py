
from eviction_policies.eviction_policy import EvictionPolicy
from typing import TypeVar
from collections import defaultdict, OrderedDict

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class LFUPolicy(EvictionPolicy[KT]):
    """Least Frequently Used eviction policy."""

    def __init__(self):
        self.freq_map = defaultdict(OrderedDict)  # Map from frequency to OrderedDict of keys
        self.key_to_freq = defaultdict(int)  # Map from key to its current frequency
        self.min_freq = 0  # Track the minimum frequency
    
    def on_get(self, key: KT) -> None:
        self._increase_frequency(key)
    
    def on_put(self, key: KT) -> None:
        if key not in self.key_to_freq:
            # New key, initialize its frequency to 1
            self.key_to_freq[key] = 1
            self.freq_map[1][key] = None  # Insert key in frequency 1 with no associated value
            self.min_freq = 1  # Reset minimum frequency to 1 for a new key
        else:
            # If key already exists, just update its frequency
            self._increase_frequency(key)
    
    def _increase_frequency(self, key: KT) -> None:
        freq = self.key_to_freq[key]
        
        # Remove the key from the current frequency's OrderedDict
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            # If we removed the last key with the minimum frequency, increase it
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Increase the frequency
        new_freq = freq + 1
        self.key_to_freq[key] = new_freq
        self.freq_map[new_freq][key] = None  
    
    def evict(self) -> KT:
        # Evict the least frequently used key (with the lowest frequency)
        if not self.freq_map[self.min_freq]:
            raise KeyError("Cache is empty, cannot evict")
        
        # Pop the least recently used key from the OrderedDict with the minimum frequency
        evicted_key, _ = self.freq_map[self.min_freq].popitem(last=False)  # Pop the first item (LRU)
        
        # Cleanup
        del self.key_to_freq[evicted_key]
        
        return evicted_key
