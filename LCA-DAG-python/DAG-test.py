import unittest
import lcaDAG


class TestLCA(unittest.TestCase):

    # tests with simple binary tree
    def test_basic_tree(self):
        tree = lcaDAG.DAG()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)
        tree.add_node(6)
        tree.add_node(7)
        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)
        tree.add_edge(3, 6)
        tree.add_edge(3, 7)

        result1 = lcaDAG.findLCA(tree.graph, 4, 5)
        result2 = lcaDAG.findLCA(tree.graph, 5, 3)
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    # Test straight tree.
    def test_straight_tree(self):
        tree = lcaDAG.DAG()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)

        tree.add_edge(1, 2)
        tree.add_edge(2, 3)
        tree.add_edge(3, 4)

        result = lcaDAG.findLCA(tree.graph, 3, 2)
        self.assertEqual(result, 2)

    # Test when one of the provided nodes is the LCA.
    def test_node_is_lca(self):
        tree = lcaDAG.DAG()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)

        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)

        result = lcaDAG.findLCA(tree.graph, 4, 2)
        self.assertEqual(result, 2)

    # Test when node is not in the tree.
    def test_node_not_included(self):
        tree = lcaDAG.DAG()
        tree.add_node(1)
        tree.add_node(2)
        tree.add_node(3)
        tree.add_node(4)
        tree.add_node(5)

        tree.add_edge(1, 2)
        tree.add_edge(1, 3)
        tree.add_edge(2, 4)
        tree.add_edge(2, 5)

        result = lcaDAG.findLCA(tree.graph, 0, 2)
        self.assertEqual(result, None)

    # Test when root is None
    def test_null_tree(self):

        tree = lcaDAG.DAG()
        result = lcaDAG.findLCA(tree.graph, 1, 2)
        self.assertEqual(result, None)


    # DAG Cases

    # Test with basic DAG.
    def test_classic_dag(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)
        dag.add_edge(1, 5)
        dag.add_edge(2, 4)
        dag.add_edge(3, 4)
        dag.add_edge(3, 5)
        dag.add_edge(4, 5)

        result = lcaDAG.findLCA(dag.graph, 2, 3)
        self.assertEqual(result, 1)

    # Test when one nodes is the LCA.
    def test_node_is_lca_dag(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)
        dag.add_edge(1, 5)
        dag.add_edge(2, 4)
        dag.add_edge(3, 4)
        dag.add_edge(3, 5)
        dag.add_edge(4, 5)

        result = lcaDAG.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, 4)

    # Test when node is not included
    def test_node_not_included_dag(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(1, 4)

        result = lcaDAG.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, None)

    # Test when the directed graph is cyclic.
    def test_cyclic_dag(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)

        dag.add_edge(1, 2)
        dag.add_edge(2, 3)
        dag.add_edge(3, 4)
        dag.add_edge(4, 1)

        result = lcaDAG.findLCA(dag.graph, 2, 3)
        self.assertEqual(result, None)

    # Tests a DAG with edges in different directions
    def test_diff_directions_dag(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        dag.add_node(2)
        dag.add_node(3)
        dag.add_node(4)
        dag.add_node(5)
        dag.add_node(6)

        dag.add_edge(1, 2)
        dag.add_edge(1, 3)
        dag.add_edge(3, 5)
        dag.add_edge(4, 2)
        dag.add_edge(5, 2)
        dag.add_edge(6, 4)
        dag.add_edge(6, 5)

        result = lcaDAG.findLCA(dag.graph, 4, 5)
        self.assertEqual(result, 6)

    # Test adding a node that already exists
    def test_adding_existing_node(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        self.assertFalse(dag.add_node(1))

    # Test adding an invalid edge
    def test_adding_invalid_edge(self):
        dag = lcaDAG.DAG()
        dag.add_node(1)
        self.assertFalse(dag.add_edge(1, 2))

if __name__ == '__main__':
    unittest.main()