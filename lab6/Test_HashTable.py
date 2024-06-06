import unittest
from HashTable import HashTable

class TestHashTable(unittest.TestCase):
    def test_insert_and_get(self):
        hash_table = HashTable()
        hash_table.insert("key1","value1" )
        hash_table.insert("key2", "value2")
        self.assertEqual(hash_table.get("key1"), "value1")
        self.assertEqual(hash_table.get("key2"), "value2")

    def test_update_existing_key(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key1", "new_value1")
        self.assertEqual(hash_table.get("key1"), "new_value1")

    def test_delete(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.delete("key1")
        self.assertRaises(KeyError, hash_table.get, "key1")
        self.assertEqual(hash_table.get("key2"), "value2")

    def test_clear(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.clear()
        self.assertEqual(len(hash_table), 0)

    def test_load_factor(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        self.assertLess(hash_table.load_factor(), 1.0)

    def test_hash_collision(self):
        hash_table = HashTable()
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        self.assertEqual(hash_table.get("key1"), "value1")
        self.assertEqual(hash_table.get("key2"), "value2")

if __name__ == '__main__':
    unittest.main()