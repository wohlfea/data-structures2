# _*_ encoding: utf-8 _*_
class BST(object):
    """Create an instance of a binary search tree."""

    def __init__(self):
        """Instantiating tree and setting marker to show if tree is empty."""
        # self._marker = object()
        self.head = None
        self.length = 0

    def _get_node(self, value):
        curnode = self.head
        while curnode.get_left_child() or curnode.get_right_child():
            if value < curnode.data and curnode.get_left_child():
                curnode = curnode.get_left_child()
            elif value > curnode.data and curnode.get_right_child():
                curnode = curnode.get_right_child()
            else:
                break
        return curnode

    def insert(self, value):
        """Add a node to the tree in the appropriate place."""
        if isinstance(value, int):
            if self.length == 0:
                self.head = BSTNode(value)
                self.length += 1
                return
            curnode = self._get_node(value)
            if value < curnode.data:
                curnode.set_left_child(BSTNode(value, curnode))
                self.length += 1
            elif value > curnode.data:
                curnode.set_right_child(BSTNode(value, curnode))
                self.length += 1
            else:
                raise ValueError('That value is already in the tree.')

        else:
            raise ValueError("You cannot insert {}".format(type(value)))

    def size(self):
        """Return the number of nodes in the tree."""
        return self.length

    def contains(self, value):
        """Check if given value is already in tree."""
        curnode = self._get_node(value)
        if curnode.data == value:
            return True
        return False


    def depth(self):
        """Calculate the depth of the tree."""
        if not self.length:
            return 0
        visited = [None]
        queue = [self.head]
        depth = 1
        cur_depth = 1

        while queue:

            while queue[-1].get_right_child() not in visited or queue[-1].get_left_child() not in visited:
                lc = queue[-1].get_left_child()
                rc = queue[-1].get_right_child()
                if rc not in visited:
                    queue.append(rc)
                    visited.append(rc)
                    cur_depth += 1
                    if depth < cur_depth:
                        depth = cur_depth
                elif lc not in visited:
                    queue.append(lc)
                    visited.append(lc)
                    cur_depth += 1
                    if depth < cur_depth:
                        depth = cur_depth
            queue.pop()
            cur_depth -= 1
        return depth




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
