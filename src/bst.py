# _*_ encoding: utf-8 _*_
# import timeit
from timeit import default_timer as timer
from collections import deque


class BST(object):
    """Create an instance of a binary search tree."""

    def __init__(self):
        """Instantiating tree and setting marker to show if tree is empty."""
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

    def depth(self, node=None):
        """Calculate the depth of the tree."""
        node = node or self.head
        if not self.length:
            return 0
        visited = [None]
        queue = [node]
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

    def balance(self):
        """Return a value based on balance of tree."""
        right_balance = 0
        left_balance = 0
        if not self.head:
            return 0
        if self.head.right_child:
            right_balance = self.depth(self.head.right_child)
        if self.head.left_child:
            left_balance = self.depth(self.head.left_child)
        difference = left_balance - right_balance
        if not difference:
            return 0
        return difference / abs(difference)


    def preorder(self, node):
        yield node.data
        if node.get_left_child():
            for item in self.preorder(node.left_child):
                yield item
        if node.get_right_child():
            for item in self.preorder(node.right_child):
                yield item


    def inorder(self, node):
        if node.left_child:
            for item in self.inorder(node.left_child):
                yield item
        yield node.data
        if node.right_child:
            for item in self.inorder(node.right_child):
                yield item

    def post_order(self, node):
        if node.left_child:
            for item in self.post_order(node.left_child):
                yield item
        if node.right_child:
            for item in self.post_order(node.right_child):
                yield item
        yield node.data

    def breadth_first(self, node):
        queue = deque((node,))
        while queue:
            node = queue.pop()
            yield node.data
            if node.left_child:
                queue.appendleft(node.left_child)
            if node.right_child:
                queue.appendleft(node.right_child)




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


if __name__ == '__main__':
    new_bst = BST()
    new_bst.insert(20)
    new_bst.insert(22)
    new_bst.insert(14)
    new_bst.insert(17)
    new_bst.insert(21)
    new_bst.insert(3)
    new_bst.insert(6)
    print('Search for head value:')
    start = timer()
    new_bst.contains(20)
    end = timer()
    best = end - start
    start1 = timer()
    new_bst.contains(6)
    end1 = timer()
    worst = end1 - start1
    print('Best case: {}\nWorst case: {}'.format(best, worst))
    # print(new_bst.preorder(new_bst.head))
    print([x for x in new_bst.breadth_first(new_bst.head)])
