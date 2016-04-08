# _*_ encoding: utf-8 _*_
import pytest

NODES_IN_TREE = [(20, True), (22, True), (21, True), (14, True), (75, False),
                 (0, False), (7, False), (15, False)]


@pytest.fixture()
def populated_tree():
    """Fixture for populating BST."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(20)
    new_bst.insert(22)
    new_bst.insert(14)
    new_bst.insert(17)
    new_bst.insert(21)
    new_bst.insert(3)
    new_bst.insert(6)

    return new_bst


@pytest.fixture()
def right_balance_tree():
    """Fixture to test balance if tree is longer on left."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(30)
    new_bst.insert(60)
    new_bst.insert(40)
    new_bst.insert(50)
    new_bst.insert(45)
    new_bst.insert(10)
    new_bst.insert(8)
    new_bst.insert(15)

    return new_bst


def test_create_node():
    """Test that node can be created with right attributes."""
    from bst import BSTNode
    node = BSTNode(10)
    assert node.data == 10
    assert node.parent is None
    assert node.right_child is None
    assert node.left_child is None


def test_node_set_get():
    """Test that node attributes can be changed and accessed."""
    from bst import BSTNode
    node = BSTNode(10)
    another_node = BSTNode(15)
    node.set_right_child(another_node)
    assert node.get_right_child() is another_node


def test_new_bst():
    """Test creation of new tree."""
    from bst import BST
    new_bst = BST()
    assert not new_bst.head


def test_first_item():
    """Test that head is set to first value inserted to tree."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(10)
    assert new_bst.head.data == 10


def test_num_only():
    """Test that only numbers can be put into the tree."""
    from bst import BST
    new_bst = BST()
    with pytest.raises(ValueError):
        new_bst.insert('bananas')


def test_child_setting():
    """Test that inserting a value less than head sets right child value to head."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    new_bst.insert(3)
    assert new_bst.head.get_left_child().data == 3


def test_larger_child():
    """Test that inserting a value greater than head sets the left child of head."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    new_bst.insert(9)
    assert new_bst.head.get_right_child().data == 9


def test_insert_same():
    """Test that a value cannot be added to tree if it already exisits."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    with pytest.raises(ValueError):
        new_bst.insert(5)


@pytest.mark.parametrize('value, result', NODES_IN_TREE)
def test_contains(populated_tree, value, result):
    """Test that contains method returns correct T/F correctly if node is/isn't in tree."""
    assert populated_tree.contains(value) == result


def test_not_contains(populated_tree):
    """Test that a value is not in tree."""
    assert not populated_tree.contains(1)


def test_size_empty():
    """Test that size of empty tree is 0."""
    from bst import BST
    new_bst = BST()
    assert new_bst.size() == 0


def test_size_not_empty(populated_tree):
    """Test that size of populated tree is returned correctly."""
    assert populated_tree.size() == 7


def test_depth(populated_tree):
    """Test depth of populated tree."""
    assert populated_tree.depth() == 4


def test_balance(populated_tree):
    """Test balance of left higher tree."""
    assert populated_tree.balance() == 1


def test_balance_empty_tree():
    """Test balance of empty tree."""
    from bst import BST
    new_bst = BST()
    assert new_bst.balance() == 0


def test_balance_1_node():
    """Test balance of tree of only head."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(10)
    assert new_bst.balance() == 0


def test_right_tree(right_balance_tree):
    """Test balance of right higher tree."""
    assert right_balance_tree.balance() == -1
