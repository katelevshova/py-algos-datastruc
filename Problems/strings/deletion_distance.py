"""
TASK: Find deletion distance between 2 strings.
Levenshtein distance is a string metric for measuring the difference between two sequences.
Informally, the Levenshtein distance between two words is the minimum number
of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

The Levenshtein distance has several simple upper and lower bounds. These include:

    It is at least the difference of the sizes of the two strings.
    It is at most the length of the longer string.
    It is zero if and only if the strings are equal.
    If the strings are the same size, the Hamming distance is an upper bound on the Levenshtein distance.
        The Hamming distance is the number of positions at which the corresponding
        symbols in the two strings are different.
    The Levenshtein distance between two strings is no greater than the sum of their Levenshtein distances
        from a third string (triangle inequality).


The deletion distance between two strings is the minimum sum of ASCII values of characters
that you need to delete in the two strings in order to have the same string.
The deletion distance between cat and at is 99, because you can just delete the first
character of cat and the ASCII value of 'c' is 99.
The deletion distance between cat and bat is 98 + 99, because you need to delete the first character of both words.
Of course, the deletion distance between two strings can't be greater than the sum of their total ASCII values,
because you can always just delete both of the strings entirely.
Implement an efficient function to find the deletion distance between two strings.

For example:
str1="thought", str2="sloughs"
Both strings have 'ough' so we need to delete 'th' and 't' from str1 (3 chars) and 'sl' and 's' from str2 (3 chars),
in total we need to remove 6 chars which is our deletion distance.
"""


def deletion_distance(str1: str, str2: str) -> int:
    print("->deletion_distance: str1={}, str2={}".format(str1, str2))
    cur = list(range(len(str2) + 1))
    prev = [0] * (len(str2) + 1)

    # print(cur)
    # print(prev)

    for i in range(len(str1)):
        # print("i="+str(i))
        cur, prev = prev, cur
        # print("cur={}, prev={}".format(cur, prev))
        cur[0] = i + 1
        # print(cur[0])
        for j in range(len(str2)):
            # Substitution is same as two deletions
            if str1[i] == str2[j]:
                sub = 0
            else:
                sub = 2
            # print("sub="+str(sub))
            cur[j + 1] = min(prev[j] + sub, cur[j] + 1, prev[j + 1] + 1)

    return cur[-1]


def test_deletion_distance_1():
    print("->test_deletion_distance_1: start")
    result = deletion_distance("cat", "at")
    expected = 1  # we need to remove only 'c' from str1
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_1: end\n")


def test_deletion_distance_2():
    print("->test_deletion_distance_2: start")
    result = deletion_distance("catb", "at")
    expected = 2
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_2: end\n")


def test_deletion_distance_3():
    print("->test_deletion_distance_3: start")
    result = deletion_distance("thought", "sloughs")
    expected = 6  # 'th' and 't' from str1 (3 chars) and 'sl' and 's' from str2 (3 chars), total = 6
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_3: end\n")


def test_deletion_distance_4():
    print("->test_deletion_distance_4: start")
    result = deletion_distance("boom", "")
    expected = 4
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_4: end\n")


def test_deletion_distance_5():
    print("->test_deletion_distance_5: start")
    result = deletion_distance("", "flower")
    expected = 6
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_5: end\n")


def test_deletion_distance_6():
    print("->test_deletion_distance_6: start")
    result = deletion_distance("", "")
    expected = 0
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_6: end\n")


def test_deletion_distance_7():
    print("->test_deletion_distance_7: start")
    result = deletion_distance("book", "book")
    expected = 0
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_7: end\n")


def test():
    test_deletion_distance_1()
    test_deletion_distance_2()
    test_deletion_distance_3()
    test_deletion_distance_4()
    test_deletion_distance_5()
    test_deletion_distance_6()
    test_deletion_distance_7()
    print("======================")
    print("ALL TEST CASES FINISHED")


test()
