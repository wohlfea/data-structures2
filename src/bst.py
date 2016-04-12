# _*_ encoding: utf-8 _*_
# import timeit
from timeit import default_timer as timer
from collections import deque
import io
import random
# from math import random


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
        # return curnode.data == value
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

    def balance(self, node=None):
        """Return a value based on balance of tree."""
        node = node or self.head
        right_balance = 0
        left_balance = 0
        if not self.head:
            return 0
        if node.right_child:
            right_balance = self.depth(node.right_child)
        if self.head.left_child:
            left_balance = self.depth(node.left_child)
        difference = right_balance - left_balance
        if not difference:
            return 0
        return difference / abs(difference)

    def preorder(self, node):
        yield node.data
        # import pdb; pdb.set_trace()

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

    def delete_node(self, val):
        # fix to not call _get_node twice
        if not self.contains(val):
            return
        node = self._get_node(val)
        # if node is head
        child_count = len([x for x in [node.left_child, node.right_child] if x])
        if not child_count:
            self._childless(node)
        elif child_count == 1:
            self._only_child(node)
        else:
            self._has_2_children(node)
        self.length -= 1

    def _has_2_children(self, node):
        balanced = self.balance(node)
        if balanced <= 0:
            target = self._get_node(min([x for x in self.breadth_first(node.right_child)]))
            if target.right_child:
                target.parent.left_child = target.right_child
                target.right_child.parent = target.parent
            else:
                target.parent.right_child = None
            target.parent = node.parent
            if node.parent.left_child is node:
                node.parent.left_child = target
            else:
                node.parent.right_child = target
        else:
            target = self._get_node(max([x for x in self.breadth_first(node.left_child)]))
            if target.left_child:
                target.parent.right_child = target.left_child
                target.left_child.parent = target.parent
            else:
                target.parent.right_child = None
            target.parent = node.parent
            if node.parent.left_child is node:
                node.parent.left_child = target
            else:
                node.parent.right_child = target

        if node.left_child is not target:
            try:
                node.left_child.parent = target
            except AttributeError:
                pass
            target.left_child = node.left_child
        if node.right_child is not target:
            try:
                node.right_child.parent = target
            except AttributeError:
                pass

            target.right_child = node.right_child
        node.parent = node.left_child = node.right_child = None

    def _childless(self, node):
        if node.parent.left_child is node:
            node.parent.left_child = None
        else:
            node.parent.right_child = None
        node.parent = None

    def _only_child(self, node):
        if node.left_child:
            # child = node.left_child
            # else child = node.right
            # get parent (getattr(node.parent))
            node.left_child.parent = node.parent
            if node.parent.left_child is node:
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child

        else:
            node.right_child.parent = node.parent
            if node.parent.left_child is node:
                node.parent.left_child = node.right_child

            else:
                node.parent.right_child = node.right_child
        node.right_child = node.parent = node.left_child = None


    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.head.data is None else (
            "\t%s;\n%s\n" % (
                self.head.data,
                "\n".join(self.head._get_dot())
            )
        ))



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

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left_child is not None:
            yield "\t%s -> %s;" % (self.data, self.left_child.data)
            for i in self.left_child._get_dot():
                yield i
        elif self.right_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right_child is not None:
            yield "\t%s -> %s;" % (self.data, self.right_child.data)
            for i in self.right_child._get_dot():
                yield i
        elif self.left_child is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)


if __name__ == '__main__':
    import subprocess
    new_bst = BST()
    # new_bst.insert(20)
    # new_bst.insert(22)
    # new_bst.insert(14)
    # new_bst.insert(17)
    # new_bst.insert(21)
    # new_bst.insert(3)
    # new_bst.insert(6)
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
    new_bst.delete_node(250)
    # print('Search for head value:')
    # start = timer()
    # new_bst.contains(20)
    # end = timer()
    # best = end - start
    # start1 = timer()
    # new_bst.contains(6)
    # end1 = timer()
    # worst = end1 - start1
    # print('Best case: {}\nWorst case: {}'.format(best, worst))
    # # print(new_bst.preorder(new_bst.head))
    # print([x for x in new_bst.breadth_first(new_bst.head)])
    # data = new_bst.get_dot()
    # with io.open('outfile', 'w') as file:
    #     file.write(data)
    dot_graph = new_bst.get_dot()
    dot_graph = dot_graph.encode('utf-8')
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
