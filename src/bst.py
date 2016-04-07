# _*_ encoding: utf-8 _*_
class BST(object):
    """Create an instance of a binary search tree."""

    def __init__(self):
        """Instantiating tree and setting marker to show if tree is empty."""
        self._marker = object()
        self.head = self._marker

    def insert(self, value):
        """Add a node to the tree in the appropriate place."""
        if isinstance(value, int):
            if self.head == self._marker:
                self.head = BSTNode(value)
                return
            curnode = self.head
            while curnode.get_left_child() or curnode.get_right_child():
                if value < curnode.data and curnode.get_left_child():
                    curnode = curnode.get_left_child()
                elif value > curnode.data and curnode.get_right_child():
                    curnode = curnode.get_right_child()
                else:
                    break
            if value < curnode.data:
                curnode.set_left_child(BSTNode(value, curnode))
            elif value > curnode.data:
                curnode.set_right_child(BSTNode(value, curnode))
            else:
                raise ValueError('That value is already in the tree.')

        else:
            raise ValueError("You cannot insert {}".format(type(value)))


class BSTNode(object):
    """Create an instance of a node for the binary search tree."""

    def __init__(self, data, parent=None):
        """Instantiate bstnode."""
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def set_parent(self, parent):
        """Set parent value for a node."""
        self.parent = parent

    def set_left_child(self, child):
        """Set the left child for a node."""
        self.left_child = child

    def set_right_child(self, child):
        """Set the right child for a node."""
        self.right_child = child

    def get_parent(self):
        """Get parent value for a node."""
        return self.parent

    def get_left_child(self):
        """Get the left child for a node."""
        return self.left_child

    def get_right_child(self):
        """Get the right child for a node."""
        return self.right_child
