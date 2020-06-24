"""
TASK6:
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects
that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either
the union or intersection, respectively. Once you have completed the problem you will create
your own test cases and perform your own run time analysis on the code.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Node: " + str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value)

            if cur_head.next is not None:
                out_string += " -> "

            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


class ListOperations:

    def union(self, linked_list_1, linked_list_2) -> LinkedList:
        # print("->union:")
        # print("linked_list_1= " + str(linked_list_1))
        # print("linked_list_2= " + str(linked_list_2))

        union_set = set()
        node1 = linked_list_1.head
        node2 = linked_list_2.head
        # print("node1= " + str(node1) + ", value=" + str(node1.value))
        # print("node2= " + str(node2) + ", value=" + str(node2.value))

        while node1 != None or node2 != None:
            if node1 != None:
                union_set.add(node1.value)
                node1 = node1.next
            if node2 != None:
                union_set.add(node2.value)
                node2 = node2.next

        # print("union_set= " + str(union_set))
        return self.convert_set_to_linked_list(union_set)

    def convert_set_to_linked_list(self, _set) -> LinkedList:
        result_list = LinkedList()
        for item in _set:
            result_list.append(item)
        return result_list

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x, linked_list):

        # Initialize current to head
        current = linked_list.head

        # loop till current not equal to None
        while current != None:
            if current.value == x:
                return True  # data found

            current = current.next

        return False  # Data Not found

    def intersection(self, linked_list_1, linked_list_2):
        print("->intersection:")


# TEST CASES: start----------------------------------------------
def test_convert_set_to_linked_list():
    print("->test_convert_set_to_linked_list: start")

    listOperations = ListOperations()
    test_set = set({1, 7, 5, 4})
    result_linked_list = listOperations.convert_set_to_linked_list(test_set)
    # print("result_linked_list= "+str(result_linked_list))

    node = result_linked_list.head

    while node is not None:
        assert node.value in test_set
        node = node.next
    print("->test_convert_set_to_linked_list: end")


def test_union_1():
    print("->test_union_1: start")

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    listOperations = ListOperations()

    assert linked_list_1.size() == len(element_1)
    assert linked_list_2.size() == len(element_2)

    # all uniqie from ll2, all unique from ll1, both unique
    expected_union_linked_list = listOperations.convert_set_to_linked_list(
        set(element_1).union(set(element_2)))  # [32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21]
    result_union_linked_list = listOperations.union(linked_list_1, linked_list_2)
    print("expected_union_linked_list= " + str(expected_union_linked_list))
    print("result_union_linked_list= " + str(result_union_linked_list))

    assert expected_union_linked_list.size() == result_union_linked_list.size()
    node = expected_union_linked_list.head
    while node != None:
        assert listOperations.search(node.value, result_union_linked_list)
        node = node.next

    print("->test_union_1: end")


def test_union_2():
    print("->test_union_2: start")
    print("->test_union_2: end")


# TEST CASES: end----------------------------------------------

def test():
    test_convert_set_to_linked_list()
    test_union_1()


test()
