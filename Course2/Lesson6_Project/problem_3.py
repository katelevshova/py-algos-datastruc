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
        self.heap = []
        self.left = None
        self.right = None

    def set_value(self, char, freq: int):
        self.char = char
        self.freq = freq

    def get_value(self) -> tuple:
        return self.char, self.freq

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

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class HuffmanCoding():

    def __init__(self, mess):
        self.message = mess
        self.heap_list = []
        self.codes = {}

    def huffman_encoding(self):
        print("->huffman_encoding:")

        # 1. Determine the frequency of each character in the message
        frequency_dict = self.create_frequency_dict(test_message)
        # 2. We would need our list to work as a priority queue,
        # where a node that has lower frequency should have a higher priority to be popped-out.
        sorted_ordered_dict = self.convert_to_sorted_ordered_dict(frequency_dict)
        # 3. Build a Huffman tree
        self.build_huffman_tree(sorted_ordered_dict)

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

    def convert_to_sorted_ordered_dict(self, dictionary: dict):
        print("-> convert_to_sorted_ordered_dict:")
        for key, value in dictionary.items():
            print(key, '->', value)

        # dictionary sorted by value
        sorted_dict = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))

        print("--------------------")
        for key, value in sorted_dict.items():
            print(key, '->', value)

        return sorted_dict

    def build_huffman_tree(self, sorted_ordered_dict: OrderedDict):
        print("-> build_huffman_tree: ")
        for key in sorted_ordered_dict:
            node = HeapNode(key, sorted_ordered_dict[key])
            heapq.heappush(self.heap_list, node)






def main():
    huffman_codding = HuffmanCoding(test_message)
    huffman_codding.huffman_encoding()


main()
