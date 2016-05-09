# _*_ encoding: utf-8 _*_


class LinkedList(object):
    """Demonstrate linked list."""

    def __init__(self, val=None):
        """Initialize the list."""
        self.head = object()
        self._mark = self.head
        if val:
            self.insert(val)

    def insert(self, val):
        """Insert value at head of list."""
        if type(val) == list:
            for item in val:
                new_node = Node(item, self.head)
                self.head = new_node
        else:
            new_node = Node(val, self.head)
            self.head = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        item = self.head
        if item is self._mark:
            raise IndexError
        else:
            self.head = item.get_next()
            return item.get_data()

    def size(self):
        """Return the length of the list."""
        counter = 0
        current_node = self.head
        while current_node is not self._mark:
            counter += 1
            current_node = current_node.get_next()
        return counter

    def search(self, val):
        """Return the node containing 'val' in list if exists, else None."""
        current_node = self.head
        while current_node.get_data() is not val:
            current_node = current_node.get_next()
            if current_node is self._mark:
                raise IndexError
        return current_node
        print("Found it!")

    def remove(self, val):
        """Remove given node from list."""
        previous_node = None
        current_node = self.head
        while current_node.get_data() is not val.get_data():
            previous_node = current_node
            current_node = current_node.get_next()
            if current_node.get_data() is None:
                break
        if current_node.get_data() == val.get_data():
            try:
                previous_node.set_next(current_node.get_next())
            except:
                return self.pop()
        else:
            print('Not Found')

    def display(self):
        """Print list represented as Python tuple literal."""
        output = """"""
        current_node = self.head
        while current_node is not self._mark:
            output += '{}, '.format(current_node.get_data())
            current_node = current_node.get_next()
        printable = '(' + output[:-2] + ')'
        print(printable)
        return printable

    def reverse(self):
        """Reverse the linked list."""
        prev = self._mark
        cur = self.head
        while cur is not self._mark:
            prev, cur.next_node, cur = cur, prev, cur.next_node
        self.head = prev


class Node(object):
    """Node constructor for linked list."""

    def __init__(self, data=None, next_node=None):
        """Initialize the node."""
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Get data for node."""
        return self.data

    def get_next(self):
        """Retrieve next node in list."""
        return self.next_node

    def set_next(self, next_node):
        """Set next node in list."""
        self.next_node = next_node
