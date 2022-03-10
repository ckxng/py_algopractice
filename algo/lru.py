class LRUElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:
    """
    a cache containing the most recently accessed elements
    """

    def __init__(self, capacity):
        """
        :param capacity: the number of elements to store in the cache
        """
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
        """
        get an element from the cache by key, or raise KeyError if the element is not found
        :param x: the key to fetch
        :return: the content related to that key
        """
        # raises exception if key not found
        index = self.__lookup_index_by_key(x)

        # move this item to the front of the cache
        # to delay it from being removed
        self.__shift_to_front(index)

        # prune if needed
        self.__prune()

        return self.__cache[0].value

    def set(self, x, y):
        """
        add an element to the cache.  if the cache is already at-capacity, the least recently
        accessed element will be removed
        :param x: the key of the object to cache
        :param y: the content of the object to cache
        """
        self.__cache.insert(0, LRUElement(x, y))
        self.__prune()
