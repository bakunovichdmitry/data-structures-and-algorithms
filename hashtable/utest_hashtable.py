import unittest

import hash_function

hashtable_test = hash_function.HashTable()


class HashTableTestCase(unittest.TestCase):
    def test_add(self):
        key = ['a', 'b', 'bb', 'c', 'd', 'e', 'f', 'g', 'h']
        values = ['a', 'b', 'bb', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(len(key)):
            hashtable_test[key[i]] = values[i]

        for i in range(len(key)):
            self.assertEqual(hashtable_test[key[i]], values[i])

    def test_delete(self):
        key = ['a', 'b', 'bb', 'c', 'd', 'e', 'f', 'g', 'h']

        for i in range(len(key)):
            del hashtable_test[key[i]]

        for i in range(len(key)):
            self.assertEqual(hashtable_test[key[i]], False)


if __name__ == '__main__':
    unittest.main()
