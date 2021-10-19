import unittest
import lca

class LCATest(unittest.TestCase):

    # Test basic LCA queries with binary tree.
    def test_basic_tree(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result1 = lca.findLCA(root, 4, 5).key
        result2 = lca.findLCA(root, 5, 3).key

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    # Test straight binary tree.
    def test_straight_tree(self):
        root = lca.Node(1)
        root.right = lca.Node(2)
        root.right.right = lca.Node(3)
        root.right.right.right = lca.Node(4)

        result = lca.findLCA(root, 4, 3).key
        self.assertEqual(result, 3)

    # Test when one of the provided nodes is the LCA.
    def test_node_is_lca(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)

        result = lca.findLCA(root, 4, 2).key
        self.assertEqual(result, 2)

    # Test when provided node is not in the binary tree.
    def test_node_not_included(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)

        result = lca.findLCA(root, 0, 2)
        self.assertEqual(result, None)

    # Test when there is no binary tree (root is None).
    def test_null_tree(self):
        root = None
        result = lca.findLCA(root, 1, 2)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()