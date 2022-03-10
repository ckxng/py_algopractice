class LRUElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.__cache = []

    def __shift_to_front(self, index):
        val = self.__cache.pop(index)
        self.__cache.insert(0, val)

    def __lookup_index_by_key(self, x):
        for i in range(len(self.__cache)):
            if self.__cache[i].key == x:
                return i

        raise KeyError()

    def __prune(self):
        cache_size = len(self.__cache)
        if cache_size > self.capacity:
            del self.__cache[cache_size - 1]

    def get(self, x):
        # raises exception if key not found
        index = self.__lookup_index_by_key(x)

        # move this item to the front of the cache
        # to delay it from being removed
        self.__shift_to_front(index)

        # prune if needed
        self.__prune()

        return self.__cache[0].value

    def set(self, x, y):
        self.__cache.insert(0, LRUElement(x, y))
        self.__prune()
