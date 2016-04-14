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


@pytest.fixture()
def another_tree():
    from bst import BST
    new_bst = BST()
    new_bst.insert(50)
    new_bst.insert(200)
    new_bst.insert(250)
    new_bst.insert(240)
    new_bst.insert(275)
    new_bst.insert(150)
    new_bst.insert(175)
    new_bst.insert(235)
    new_bst.insert(245)
    new_bst.insert(237)
    new_bst.insert(100)

    return new_bst


@pytest.fixture()
def tiny_tree():
    from bst import BST
    new_bst = BST()
    new_bst.insert(30)
    new_bst.insert(50)
    new_bst.insert(75)

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
    """Test that inserting a value less than
    head sets right child value to head."""
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    new_bst.insert(3)
    assert new_bst.head.get_left_child().data == 3


def test_larger_child():
    """Test that inserting a value greater than
    head sets the left child of head."""
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
    """Test that contains method returns correct T/F
    correctly if node is/isn't in tree."""
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
    assert right_balance_tree.balance() == 1


def test_preorder(populated_tree):
    assert [x for x in populated_tree.preorder(populated_tree.head)] == [20, 14, 3, 6, 17, 22, 21]


def test_preorder2(right_balance_tree):
    assert [x for x in right_balance_tree.preorder(right_balance_tree.head)] == [40, 10, 8, 30, 15, 50, 45, 60]


def test_inorder(populated_tree):
    assert [x for x in populated_tree.inorder(populated_tree.head)] == [3, 6, 14, 17, 20, 21, 22]


def test_inorder2(right_balance_tree):
    assert [x for x in right_balance_tree.inorder(right_balance_tree.head)] == [8, 10, 15, 30, 40, 45, 50, 60]


def test_post_order(populated_tree):
    assert [x for x in populated_tree.post_order(populated_tree.head)] == [6, 3, 17, 14, 21, 22, 20]


def test_post_order2(right_balance_tree):
    assert [x for x in right_balance_tree.post_order(right_balance_tree.head)] ==  [8, 15, 30, 10, 45, 60, 50, 40]


def test_breadth(populated_tree):
    assert [x for x in populated_tree.breadth_first(populated_tree.head)] == [20, 14, 22, 3, 17, 21, 6]


def test_breadth2(right_balance_tree):
    assert [x for x in right_balance_tree.breadth_first(right_balance_tree.head)] == [40, 10, 50, 8, 30, 45, 60, 15]


def test_remove_childless_node(populated_tree):
    assert populated_tree.contains(6)
    populated_tree.delete_node(6)
    assert not populated_tree.contains(6)


def test_remove_childless_node_tree_intact(populated_tree):
    assert populated_tree.contains(6)
    populated_tree.delete_node(6)
    assert [x for x in populated_tree.breadth_first(populated_tree.head)] == [20, 14, 22, 3, 17, 21]


def test_remove_1_child(populated_tree):
    assert populated_tree.contains(3)
    populated_tree.delete_node(3)
    assert not populated_tree.contains(3)
    assert [x for x in populated_tree.breadth_first(populated_tree.head)] == [20, 14, 22, 6, 17, 21]


def test_remove_1_child_tree(populated_tree):
    assert populated_tree.contains(3)
    populated_tree.delete_node(3)
    assert [x for x in populated_tree.breadth_first(populated_tree.head)] == [20, 14, 22, 6, 17, 21]


def test_delete_2_children(another_tree):
    assert another_tree.contains(250)
    another_tree.delete_node(250)
    assert not another_tree.contains(250)

def test_delete_2_children_tree(another_tree):
    assert another_tree.contains(250)
    another_tree.delete_node(250)
    assert [x for x in another_tree.preorder(another_tree.head)] == [200, 150, 50, 100, 175, 240, 235, 237, 245, 275]


def test_delete_2_child_tree_1(right_balance_tree):
    assert right_balance_tree.contains(10)
    right_balance_tree.delete_node(10)
    assert not right_balance_tree.contains(10)
    assert [x for x in right_balance_tree.preorder(right_balance_tree.head)] == [40, 15, 8, 30, 50, 45, 60]


def test_balance_insert(tiny_tree):
    """Test that tree balances on insert for right right unbalance."""
    assert tiny_tree.head.data == 50


def test_balance_insert_again(tiny_tree):
    """Test that insert balance in RR works repeatedly."""
    an_order = [x for x in tiny_tree.inorder(tiny_tree.head)]
    tiny_tree.insert(100)
    tiny_tree.insert(150)
    assert [x for x in tiny_tree.inorder(tiny_tree.head)] == an_order + [100, 150]


def test_new_tree():
    from bst import BST
    new_bst = BST()
    new_bst.insert(100)
    new_bst.insert(25)
    new_bst.insert(30)
    new_bst.insert(40)
    assert [x for x in new_bst.inorder(new_bst.head)] == [25, 30, 40, 100]
