import unittest
import lru


class TestLRU(unittest.TestCase):
    def test_lru(self):
        cache = lru.LRUCache(5)
        cache.set('a', 'A')
        cache.set('b', 'B')
        cache.set('c', 'C')
        cache.set('d', 'D')
        cache.set('e', 'E')
        self.assertEqual(cache.get('a'), 'A')
        cache.set('f', 'F')
        self.assertRaises(KeyError, cache.get, 'b')


if __name__ == '__main__':
    unittest.main()
