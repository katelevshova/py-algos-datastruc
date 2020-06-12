# TASK
'''
Given a sentence, reverse each word in the sentence while keeping the order the same!
'''


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    words_list = our_string.split(" ")
    result_str = ""

    for word in words_list:
        for i in range(len(word)):
            result_str += word[(len(word) - 1) - i]
        result_str += " "

    print("our_string={}, result_str={}".format(our_string, result_str))
    return result_str.strip()
    pass

'''
Other solution:
    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)
'''

# Test Cases

print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
