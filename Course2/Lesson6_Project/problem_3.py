"""
TASK3:
Huffman Coding:
A. Huffman Encoding
B. Huffman Decoding
"""
test_message = "AAAAAAABBBCCCCCCCDDEEEEEE"


def huffman_encoding():
    # 1. Determine the frequency of each character in the message
    create_frequency_dict(test_message)


def create_frequency_dict(message) -> dict:
    print("->create_frequency_dict: message={}".format(message))
    frequency_dict = {char: message.count(char) for char in set(message)}
    print("frequency_dict is :\n {}".format(str(frequency_dict)))


def main():
    huffman_encoding()


main()
