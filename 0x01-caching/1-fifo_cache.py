from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a class for caching information using FIFO strategy
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            key: Key
            item: Item
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                removed_key = self.queue.pop(0)
                del self.cache_data[removed_key]
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
