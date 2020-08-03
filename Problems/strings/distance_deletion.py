"""
TASK: Find deletion distance between 2 strings.

For example.
Input: str1="thought", str2="sloughs"
Output: 6
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


def test_edit_distance_8():
    print("->test_edit_distance_8: start")
    result = deletion_distance("kitten", "sitting")
    expected = 5
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_edit_distance_8: end\n")


def test():
    test_deletion_distance_1()
    test_deletion_distance_2()
    test_deletion_distance_3()
    test_deletion_distance_4()
    test_deletion_distance_5()
    test_deletion_distance_6()
    test_deletion_distance_7()
    test_edit_distance_8()
    print("======================")
    print("ALL TEST CASES FINISHED")


test()
