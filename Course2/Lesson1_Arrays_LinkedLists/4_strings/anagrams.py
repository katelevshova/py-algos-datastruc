# TASK
'''
The goal of this exercise is to write some code to determine if two strings are anagrams of each other.

An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

For example:

    "rat" is an anagram of "art"
    "alert" is an anagram of "alter"
    "Slot machines" is an anagram of "Cash lost in me"

Your function should take two strings as input and return True if the two words are anagrams and False if they are not.

You can assume the following about the input strings:

    No punctuation
    No numbers
    No special characters

Note - You can use built-in methods len(), lower() and sort() on strings.

'''


# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    # Clean strings
    clean_str_1 = str1.replace(" ", "").lower()
    clean_str_2 = str2.replace(" ", "").lower()

    if len(clean_str_1) == len(clean_str_2):
        if sorted(clean_str_1) == sorted(clean_str_2):
            return True

    return False

    pass


# Test Cases
print("Pass" if (anagram_checker('rat', 'art')) else "Fail")
print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")