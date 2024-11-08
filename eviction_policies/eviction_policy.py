from abc import ABC, abstractmethod
from typing import Generic, TypeVar

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type

class EvictionPolicy(ABC, Generic[KT]):
    """Abstract base class for cache eviction policies."""
    
    @abstractmethod
    def on_get(self, key: KT) -> None:
        """Called when a key is accessed."""
        pass
    
    @abstractmethod
    def on_put(self, key: KT) -> None:
        """Called when a key is added."""
        pass
    
    @abstractmethod
    def evict(self) -> KT:
        """Returns the key to be evicted."""
        pass