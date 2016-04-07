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


def test_new_bst():
    from bst import BST
    new_bst = BST()
    assert not new_bst.head


def test_first_item():
    from bst import BST
    new_bst = BST()
    new_bst.insert(10)
    assert new_bst.head.data == 10


def test_num_only():
    from bst import BST
    new_bst = BST()
    with pytest.raises(ValueError):
        new_bst.insert('bananas')


def test_child_setting():
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    new_bst.insert(3)
    assert new_bst.head.get_left_child().data == 3


def test_larger_child():
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    new_bst.insert(9)
    assert new_bst.head.get_right_child().data == 9


def test_insert_same():
    from bst import BST
    new_bst = BST()
    new_bst.insert(5)
    with pytest.raises(ValueError):
        new_bst.insert(5)


@pytest.mark.parametrize('value, result', NODES_IN_TREE)
def test_contains(populated_tree, value, result):
    assert populated_tree.contains(value) == result


def test_not_contains(populated_tree):
    assert not populated_tree.contains(1)


def test_size_empty():
    from bst import BST
    new_bst = BST()
    assert new_bst.size() == 0


def test_size_not_empty(populated_tree):
    assert populated_tree.size() == 7


def test_depth(populated_tree):
    assert populated_tree.depth() == 4
