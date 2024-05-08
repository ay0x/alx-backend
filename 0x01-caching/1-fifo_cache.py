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

    def put(self, key, item):
        """Store a key-value pair"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first key entered (FIFO)
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
