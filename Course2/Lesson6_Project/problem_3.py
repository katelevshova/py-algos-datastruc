"""
TASK3:
Huffman Coding:
A. Huffman Encoding
B. Huffman Decoding
"""
from collections import OrderedDict

test_message = "AAAAAAABBBCCCCCCCDDEEEEEE"
freq_dict = dict()


def huffman_encoding():
    # 1. Determine the frequency of each character in the message
    frequency_dict = create_frequency_dict(test_message)
    # 2. We would need our list to work as a priority queue,
    # where a node that has lower frequency should have a higher priority to be popped-out.
    sorted_ordered_dict = convert_to_sorted_ordered_dict(frequency_dict)


def create_frequency_dict(message) -> dict:
    print("->create_frequency_dict: message={}".format(message))
    frequency_dict = {char: message.count(char) for char in set(message)}
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


def convert_to_sorted_ordered_dict(dictionary):
    for key, value in dictionary.items():
        print(key, '->', value)

    # dictionary sorted by value
    sorted_dict = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1]))

    print("--------------------")
    for key, value in sorted_dict.items():
        print(key, '->', value)

    return sorted_dict


def main():
    huffman_encoding()


main()
