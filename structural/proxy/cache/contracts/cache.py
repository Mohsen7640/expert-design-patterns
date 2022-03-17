from abc import ABC, abstractmethod


class CacheInterface(ABC):
    @abstractmethod
    def get(self, key):
        """Return cached value in service"""
        pass

    @abstractmethod
    def set(self, key, value):
        """Cache value in service"""
        pass

    @abstractmethod
    def delete(self, key):
        """Delete cached value in service"""
        pass

    @abstractmethod
    def clear(self):
        """Clear all cached values in service"""
        pass
