# TASK
'''
Linked List Practice

Implement a linked list class. You have to define a few functions that perform
the desirbale action. Your LinkedList class should be able to:

    Append data to the tail of the list and prepend to the head
    Search the linked list for a value and return the node
    Remove a node
    Pop, which means to return the first node's value and delete the node from the list
    Insert data at some position in the list
    Return the size (length) of the linked list
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list

    def __str__(self) -> str:
        result = ""
        node = self.head

        while node:
            result += str(node.value)

            if node.next is not None:
                result += " -> "
            node = node.next
        return result

    def prepend(self, value):
        """ Prepend a node to the beginning of the list """
        if self.head is None:
            self.head = Node(value)
            return
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def append(self, value):
        """ Append a node to the end of the list """
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def search(self, value):

        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return
        node = self.head
        while node.next:
            if node.value == value:
                return node
            node = node.next
        raise ValueError("Value not found in the list!")

    def remove(self, value):
        """ Delete the first node with the desired data. """
        if self.head is None:
            return
        node = self.head

        if node.value == value:
            self.head = self.head.next
            return

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value is not found in the list!")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        if self.head is None:
            return

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        node = self.head
        counter = 1
        while node.next:
            counter += 1
            node = node.next
        return counter


def test():
    test_prepend()
    test_append()
    test_search()
    test_remove()
    test_pop()
    test_insert()
    test_size()


def test_prepend():
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], "list contents: {}".format(linked_list.to_list())


def test_append():
    # Test append - 1
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 3], "list contents: {}".format(linked_list.to_list())
    # Test append - 2
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], "list contents: {}".format(linked_list.to_list())
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], "list contents: {}".format(linked_list.to_list())


def test_search():
    # Test search
    linked_list = LinkedList()
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, "list contents: {}".format(linked_list.to_list())
    assert linked_list.search(4).value == 4, "list contents: {}".format(linked_list.to_list())


def test_remove():
    linked_list = LinkedList()
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)

    linked_list.remove(1)
    assert linked_list.to_list() == [2, 4, 3], "list contents: {}".format(linked_list.to_list())
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 4], "list contents: {}".format(linked_list.to_list())
    linked_list.remove(2)
    assert linked_list.to_list() == [4], "list contents: {}".format(linked_list.to_list())


def test_pop():
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(3)
    value = linked_list.pop()
    assert value == 2, "list contents: {}".format(linked_list.to_list())
    assert linked_list.head.value == 1, "list contents: {}".format(linked_list.to_list())


def test_insert():
    # Test insert
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(4)
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], "list contents: {}".format(linked_list.to_list())
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], "list contents: {}".format(linked_list.to_list())
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], "list contents: {}".format(linked_list.to_list())

def test_size():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(4)
    assert linked_list.size() == 2, "list contents: {}".format(linked_list.to_list())

    print("------")
    print(linked_list)
    print(linked_list.to_list())

test()
