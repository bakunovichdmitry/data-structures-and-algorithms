import unittest

from binary_tree import binary_search_tree as search_tree


class BinaryTreeTestCase(unittest.TestCase):
    VALUE_FOR_TREE = [8, 3, 1, 6, 4, 7, 10, 14, 13]

    def test_add(self):
        for i in self.VALUE_FOR_TREE:
            self.assertTrue(True if search_tree.add(i) else False)

    def test_get(self):
        for i in self.VALUE_FOR_TREE:
            self.assertTrue(True if search_tree[i] else False)

    def test_remove(self):
        search_for_delete = search_tree
        for i in self.VALUE_FOR_TREE:
            del search_for_delete[i]
            self.assertFalse(True if search_tree[i] else False)


if __name__ == "__main__":
    unittest.main(failfast=True, exit=False)
