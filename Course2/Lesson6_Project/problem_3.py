"""
TASK3:
Huffman Coding:
A. Huffman Encoding
B. Huffman Decoding
"""
from collections import OrderedDict
import heapq

test_message = "AAAAAAABBBCCCCCCCDDEEEEEE"


class HeapNode(object):
    def __init__(self, char, freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def set_value(self, char, freq: int):
        self.char = char
        self.freq = freq

    def get_value(self) -> tuple:
        return self.char, self.freq

    def get_value_char(self):
        return self.char

    def get_value_freq(self) -> int:
        return self.freq

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    '''
    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq
        
        p1.__le__(p2)
        
        
    '''

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        if self.freq == other.freq:
            a = (self.char, other.char)
            sorted_a = sorted(a)
            print("sorted_a=" + str(sorted_a))
            return self.char is sorted_a[0]
        else:
            return self.freq < other.freq

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"  # prints Node(('D', 2)) or Node((None, 11))


class HuffmanCoding(object):

    def __init__(self, mess):
        self.message = mess
        self.heap_list = []
        self.binary_codes = {}
        self.encoded_data = ""

    def huffman_encoding(self):
        print("->huffman_encoding:")
        # 1. Determine the frequency of each character in the message
        frequency_dict = self.create_frequency_dict(test_message)
        # 2. We would need our list to work as a priority queue,
        # where a node that has lower frequency should have a higher priority to be popped-out.
        # 3. Build a Huffman tree
        self.build_min_tree(frequency_dict)
        # 4. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.
        self.assign_binary_codes()
        # 5. create encoded text
        self.encoded_data = self.get_encoded_data(test_message)

    def create_frequency_dict(self, message_str) -> dict:
        print("\n->create_frequency_dict: message={}".format(message_str))
        frequency_dict = {char: message_str.count(char) for char in set(message_str)}
        print("frequency_dict is :\n {}".format(str(frequency_dict)))
        '''
        (Unique) Character 	Frequency
        A 	7
        B 	3
        C 	7
        D 	2
        E 	6
        '''
        return frequency_dict

    def build_min_tree(self, freq_dict: dict):
        print("\n-> build_min_tree: ")

        for key in freq_dict:
            node = HeapNode(key, freq_dict[key])
            heapq.heappush(self.heap_list, node)
        print("heap_list=" + str(self.heap_list))
        # merge nodes
        while len(self.heap_list) > 1:
            node_left = heapq.heappop(self.heap_list)
            node_right = heapq.heappop(self.heap_list)

            node_merged = HeapNode(None, node_left.freq + node_right.freq)
            node_merged.left = node_left
            node_merged.right = node_right

            heapq.heappush(self.heap_list, node_merged)

        print("converted min tree:")
        # print("in order traversal (Left, Root, Right): current root= " + str(self.heap_list[0]))
        # self.print_inorder(self.heap_list[0])
        # print("---------------------------")
        print("post order traversal (Left, Right, Root): current root= " + str(self.heap_list[0]))
        self.print_postorder(self.heap_list[0])
        print("---------------------------")
        # print("pre order traversal (Root, Left, Right): current root= " + str(self.heap_list[0]))
        # self.print_preorder(self.heap_list[0])
        # print("---------------------------")

    def assign_binary_codes(self):
        root = heapq.heappop(self.heap_list)
        print("\n->assign_binary_codes: root= " + str(root))
        self.add_codes_recursively(root, "")
        print("binary_codes= " + str(self.binary_codes))

    def add_codes_recursively(self, curr_node: HeapNode, code):
        if curr_node is None:
            return

        # we add code only for nodes with char and frequency
        if curr_node.char is not None:
            self.binary_codes[curr_node.char] = code
            print("{} : {} : {}".format(curr_node.char, curr_node.freq, self.binary_codes[curr_node.char]))
            return

        self.add_codes_recursively(curr_node.left, code + "0")
        self.add_codes_recursively(curr_node.right, code + "1")

    def get_encoded_data(self, message):
        encoded_result = map(lambda char: self.binary_codes[char], message)
        # print("->get_encoded_data: encoded_result= "+encoded_result)
        # ->get_encoded_data: encoded_result= 1111111111111100100100110101010101010000000010101010101
        result = ''.join(encoded_result)
        print("result= " + result)
        return result

    # PRINT TREE: start --------------------------------------------------------------------------------------------------
    # A function to do inorder tree traversal
    # based on material from https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    def print_inorder(self, root):
        if root:
            # First recur on left child
            self.print_inorder(root.left)

            # then print the data of node
            if root:
                print("{} : {}".format(root.char, root.freq))
            else:
                print("None")

            # now recur on right child
            self.print_inorder(root.right)

            # A function to do postorder tree traversal

    def print_postorder(self, root):
        if root:
            # First recur on left child
            self.print_postorder(root.left)

            # the recur on right child
            self.print_postorder(root.right)

            # now print the data of node
            if root:
                print("{} : {}".format(root.char, root.freq))
            else:
                print("None")

            # A function to do preorder tree traversal

    def print_preorder(self, root):
        if root:
            # First print the data of node
            if root:
                print("{} : {}".format(root.char, root.freq))
            else:
                print("None")

            # Then recur on left child
            self.print_preorder(root.left)

            # Finally recur on right child
            self.print_preorder(root.right)


# PRINT TREE: end --------------------------------------------------------------------------------------------------


def main():
    huffman_codding = HuffmanCoding(test_message)
    huffman_codding.huffman_encoding()


# TEST CASES: start----------------------------------------------
def test():
    test_node_comparrison()


def test_node_comparrison():
    print("->test_node_comparrison: start")
    node1 = HeapNode("A", 7)
    node2 = HeapNode("B", 8)
    assert (node1 < node2)

    node1 = HeapNode("A", 7)
    node2 = HeapNode("B", 7)
    assert (node1 < node2)

    node1 = HeapNode("B", 7)
    node2 = HeapNode("A", 7)
    assert (node1 > node2)

    node1 = HeapNode("A", 4)
    node2 = HeapNode("a", 7)
    assert (node1 < node2)

    node1 = HeapNode("A", 4)
    node2 = HeapNode("a", 4)
    assert (node1 < node2)

    print("->test_node_comparrison: is finished")


# TEST CASES: end----------------------------------------------------------

test()
main()
