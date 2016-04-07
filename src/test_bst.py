# _*_ encoding: utf-8 _*_
import pytest


# new_bst = [(10)]

# @pytest.mark.parametrize()
def test_new_bst():
    from bst import BST
    new_bst = BST()
    assert new_bst.head


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
