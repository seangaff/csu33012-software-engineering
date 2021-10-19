package lca
import "testing"

// Test basic LCA queries with binary tree.
func TestBasicTree(t *testing.T) {
	root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
	root.left.left = &Node{4, nil, nil}
	root.left.right = &Node{5, nil, nil}
	root.right.left = &Node{6, nil, nil}
	root.right.right = &Node{7, nil, nil}

	tables := []struct {
        n1 int
        n2 int
        expectedLCA int
    }
	{
        {4, 5, 2},
        {4, 3, 1},
        {2, 3, 1},
        {2, 7, 1},
    }
	for _, table := range tables {
		lca := leastCommonAncestorInBST(&root, table.n1, table.n2).key
		if lca != table.expectedLCA {
			t.Errorf("LCA of %d and %d is incorrect, got %d, want %d.", table.n1, table.n2, lca, table.expectedLCA)
		}
	}
}

// Test straight binary tree.
func TestStraightTree(t *testing.T) {
	root := Node{1, nil, nil}
	root.right = &Node{2, nil, nil}
	root.right.right = &Node{3, nil, nil}
	root.right.right.right = &Node{4, nil, nil}
	lca := leastCommonAncestorInBST(&root, 4, 3).key
	if lca != 3 {
		t.Errorf("LCA is incorrect, got %d, want %d", lca, 3)
	}
}

// Test when one of the provided nodes is the LCA.
func TestNodeIsLCA(t *testing.T) {
	root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
	root.left.left = &Node{4, nil, nil}
	root.left.right = &Node{5, nil, nil}
	lca := leastCommonAncestorInBST(&root, 4, 2).key
	if lca != 2 {
		t.Errorf("LCA is incorrect, got %d, want %d", lca, 2)
	}
}

// Test whe provided node is not in the binary tree.
func TestNodeNotIncluded(t *testing.T) {
	root := Node{1, nil, nil}
	root.left = &Node{2, nil, nil}
	root.right = &Node{3, nil, nil}
	root.left.left = &Node{4, nil, nil}
	root.left.right = &Node{5, nil, nil}
	lca := leastCommonAncestorInBST(&root, 0, 2)
	if lca != nil {
		t.Errorf("LCA is incorrect, should return nil if node(s) not present in tree")
	}
}

// Test when there is no binary tree (root is nil).
func TestNullTree(t *testing.T) {
	var root *Node = nil
	lca := leastCommonAncestorInBST(root, 1, 2)
	if lca != nil {
		t.Errorf("LCA is incorrect, empty tree should return nil")
	}
}
