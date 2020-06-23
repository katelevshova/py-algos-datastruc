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
        return "Node: "+str(self.value)


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
    def union(self, linked_list_1, linked_list_2):
        print("->union:")
        print("linked_list_1= "+str(linked_list_1))
        print("linked_list_2= " + str(linked_list_2))

        result_list = LinkedList()

        if linked_list_1.size() < linked_list_2:
            current_head = linked_list_2.head
            while current_head

        return result_list

    def intersection(self, linked_list_1, linked_list_2):
        print("->intersection:")


# TEST CASES: start----------------------------------------------
def test_union_intersection_1():
    print("->test_union_intersection_1: start")

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

    # all uniqie from 2, all unique from 1, both
    expected_union = list(set(element_1).union(set(element_2)))  #[32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21]
    print("expected_union="+str(expected_union))

    result_union = listOperations.union(linked_list_1, linked_list_2)

    # assert expected_union == result_union, "expected_union is {}, actual result = {}".format(expected_union,
      #                                                                                       result_union)
    print("result_union= "+str(result_union))

    print("->test_union_intersection_1: end")


# TEST CASES: end----------------------------------------------

def test():
    test_union_intersection_1()


test()
