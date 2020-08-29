"""
TASK: Find the edit distance between two given strings.

The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other
"""


def edit_distance(str1: str, str2: str) -> int:
    print("->edit_distance: str1={}, str2={}".format(str1, str2))

    difference = 0

    if len(str1) > len(str2):
        difference = len(str1) - len(str2)
        str1 = str1[:difference]
        print("updated str1="+str1)
    if len(str2) > len(str1):
        difference = len(str2) - len(str1)
        str2 = str2[:difference]
        print("updated str2=" + str2)

    len1 = len(str1)
    len2 = len(str2)

    print("len1="+str(len1))
    print("len2=" + str(len2))

    max_len = max(len1, len2)
    print("max_len="+str(max_len))

    for i in range(max_len):
        if str1[i] != str2[i]:
            difference += 1

    return difference


def test_edit_distance_1():
    print("->test_edit_distance_1: start")
    result = edit_distance("kitten", "sitting")
    expected = 3  # substitute the "k" for "s", substitute the "e" for "i", and append a "g"
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_edit_distance_1: end\n")


def test():
    test_edit_distance_1()

    print("======================")
    print("ALL TEST CASES FINISHED")


test()