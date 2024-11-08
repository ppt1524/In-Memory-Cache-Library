import unittest
from eviction_policies.cache import Cache
from eviction_policies.fifo import FIFOPolicy

from threading import Thread

class TestFIFOPolicy(unittest.TestCase):
    def test_fifo(self):
        cache = Cache(capacity=3, eviction_policy=FIFOPolicy())
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        self.assertEqual(cache.get("key1"), "value1")
        cache.put("key4", "value4")
        self.assertEqual(cache.get("key1"), None)
        self.assertEqual(cache.get("key2"), "value2")
        self.assertEqual(cache.get("key3"), "value3")
        self.assertEqual(cache.get("key4"), "value4")

    def test_fifo_thread_safety(self):
        cache = Cache(capacity=10, eviction_policy=FIFOPolicy())

        def put_items(start, end):
            for i in range(start, end):
                cache.put(f"key{i}", f"value{i}")

        threads = []
        for i in range(4):
            t = Thread(target=put_items, args=(i*10, (i+1)*10))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        self.assertEqual(cache.size(), 10)

if __name__ == '__main__':
    unittest.main()