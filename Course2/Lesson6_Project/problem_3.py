"""
TASK3:
Huffman Coding:
A. Huffman Encoding
B. Huffman Decoding
"""
from collections import OrderedDict
import heapq
import sys


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

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        # print("self.char={}, other.char={}".format(self.char, other.char))
        if self.freq == other.freq:
            if self.char is None:
                return True
            if other.char is None:
                return False
            a = (self.char, other.char)
            sorted_a = sorted(a)
            # print("sorted_a=" + str(sorted_a))
            # print("self.char={}, sorted_a[0]={}".format(self.char, sorted_a[0]))
            # print("(self.char == sorted_a[0])="+str(self.char == sorted_a[0]))
            return self.char == sorted_a[0]
        else:
            return self.freq < other.freq

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"  # prints Node(('D', 2)) or Node((None, 11))


class HuffmanCoding(object):

    def __init__(self):
        self.heap_list = []
        self.binary_codes = {}
        self.encoded_data = ""
        self.decoded_data = ""

    def huffman_encoding(self, message):
        print("->huffman_encoding:")
        # 1. Determine the frequency of each character in the message
        frequency_dict = self.create_frequency_dict(message)
        # 2. We would need our list to work as a priority queue,
        # where a node that has lower frequency should have a higher priority to be popped-out.
        # 3. Build a Huffman tree
        self.build_min_tree(frequency_dict)
        # 4. For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.
        self.assign_binary_codes()
        # 5. create encoded text
        self.encoded_data = self.get_encoded_data(message)
        return self.encoded_data

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

    def huffman_decoding(self, encoded_message):
        print("-> huffman_decoding:")

        return self.decoded_data

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
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman_codding = HuffmanCoding()
    encoded_data = huffman_codding.huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_codding.huffman_decoding(encoded_data)


# TEST CASES: start----------------------------------------------
def test():
    test_node_comparrison()
    test_get_encoded_data()
    test_huffman_encoding()
    test_huffman_decoding()


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

    node1 = HeapNode("a", 2)
    node2 = HeapNode("D", 2)
    assert (node1 > node2)

    node1 = HeapNode(None, 5)
    node2 = HeapNode("E", 6)
    assert (node1 < node2)

    node1 = HeapNode(None, 6)
    node2 = HeapNode("E", 6)
    assert (node1 < node2)

    node1 = HeapNode("W", 3)
    node2 = HeapNode(None, 6)
    assert (node1 < node2)

    node1 = HeapNode("A", 6)
    node2 = HeapNode(None, 6)
    assert (node1 > node2)

    node1 = HeapNode(None, 10)
    node2 = HeapNode(None, 26)
    assert (node1 < node2)

    node1 = HeapNode(None, 10)
    node2 = HeapNode(None, 10)
    assert (node1 == node2)

    print("->test_node_comparrison: is finished")


def test_get_encoded_data():
    print("->get_encoded_data: start")
    message1 = "ABCD"
    HuffmanCoding.binary_codes = {'A': '1', 'B': '22', 'C': '333', 'D': '4444', 'a': '5'}
    print(HuffmanCoding.binary_codes)
    actual_code = HuffmanCoding.get_encoded_data(HuffmanCoding, message1)
    expected_code = "1223334444"
    assert actual_code == expected_code, "actual_code={}, expected_code={}".format(actual_code, expected_code)
    print("->get_encoded_data: is finished")


def test_huffman_encoding():
    print("->test_huffman_encoding: start")
    test_message = "AAAAAAABBBCCCCCCCDDEEEEEE"
    huffman_codding = HuffmanCoding()
    actual_result = huffman_codding.huffman_encoding(test_message)
    expected_result = "1010101010101000100100111111111111111000000010101010101"
    assert actual_result == expected_result, "actual_result={}, " \
                                             "expected_result={}".format(actual_result, expected_result)
    print("->test_huffman_encoding: is finished")


def test_huffman_decoding():
    print("->test_huffman_decoding: start")
    test_message = "AAAAAAABBBCCCCCCCDDEEEEEE"
    huffman_codding = HuffmanCoding()
    encoded_data = huffman_codding.huffman_encoding(test_message)
    actual_result  = huffman_codding.huffman_decoding(encoded_data)

    assert actual_result == test_message,  "actual_result={}, test_message={}".format(actual_result, test_message)

    print("->test_huffman_decoding: is finished")


# TEST CASES: end----------------------------------------------------------

test()
# main()
