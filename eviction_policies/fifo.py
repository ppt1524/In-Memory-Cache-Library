from eviction_policies.eviction_policy import EvictionPolicy
from collections import OrderedDict
from typing import TypeVar

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class FIFOPolicy(EvictionPolicy[KT]):
    """First In First Out eviction policy."""
    
    def __init__(self):
        self.order = OrderedDict()
    
    def on_get(self, key: KT) -> None:
        pass  # FIFO doesn't change order on get
    
    def on_put(self, key: KT) -> None:
        if key not in self.order:
            self.order[key] = None
    
    def evict(self) -> KT:
        return self.order.popitem(last=False)[0]