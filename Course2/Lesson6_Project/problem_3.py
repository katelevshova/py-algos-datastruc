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

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq


class HuffmanCoding(object):

    def __init__(self, mess):
        self.message = mess
        self.heap_list = []
        self.binary_codes = {}

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

    def create_frequency_dict(self, message_str) -> dict:
        print("->create_frequency_dict: message={}".format(message_str))
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
        print("-> build_min_tree: ")

        for key in freq_dict:
            node = HeapNode(key, freq_dict[key])
            heapq.heappush(self.heap_list, node)

        # merge nodes
        while len(self.heap_list) > 1:
            node_left = heapq.heappop(self.heap_list)
            node_right = heapq.heappop(self.heap_list)

            node_merged = HeapNode(None, node_left.freq + node_right.freq)
            node_merged.left = node_left
            node_merged.right = node_right

            heapq.heappush(self.heap_list, node_merged)

    def assign_binary_codes(self):
        print("->assign_binary_codes:")
        root = HeapNode(self, heapq.heappop(self.heap_list))
        self.add_codes_recursively(root, "")

    def add_codes_recursively(self, curr_node: HeapNode, code):
        if curr_node is None:
            return

        if curr_node.freq is not None:
            self.binary_codes[curr_node.char] = code
            return

        self.add_codes_recursively(curr_node.left, code + "0")
        self.add_codes_recursively(curr_node.right, code + "1")


def main():
    huffman_codding = HuffmanCoding(test_message)
    huffman_codding.huffman_encoding()


main()
