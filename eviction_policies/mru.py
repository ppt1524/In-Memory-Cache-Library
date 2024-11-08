from eviction_policies.eviction_policy import EvictionPolicy
from collections import OrderedDict
from typing import TypeVar

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class MRUPolicy(EvictionPolicy[KT]):
    """Most Recently Used eviction policy."""
    
    def __init__(self):
        self.order = OrderedDict()
    
    def on_get(self, key: KT) -> None:
        if key in self.order:
            self.order.move_to_end(key)
    
    def on_put(self, key: KT) -> None:
        if key in self.order:
            self.order.move_to_end(key)
        else:
            self.order[key] = None
    
    def evict(self) -> KT:
        return self.order.popitem(last=True)[0]