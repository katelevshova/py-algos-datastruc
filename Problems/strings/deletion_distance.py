"""
TASK: Find deletion distance between 2 strings.
For example:
str1="thought", str2="sloughs"
Both strings have 'ough' so we need to delete 'th' and 't' from str1 (3 chars) and 'sl' and 's' from str2 (3 chars),
in total we need to remove 6 chars which is our deletion distance.
"""


def deletion_distance(str1: str, str2: str) -> int:
    print("->deletion_distance: ")

    return 0


def test_deletion_distance_1():
    print("->test_deletion_distance_1: start")
    result = deletion_distance("thought", "sloughs")
    expected = 6  # 'th' and 't' from str1 (3 chars) and 'sl' and 's' from str2 (3 chars), total = 6
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_1: end")


def test_deletion_distance_2():
    print("->test_deletion_distance_2: start")
    result = deletion_distance("boom", "")
    expected = 4  # we need to remove the length of the str1
    print("result={}, expected={}".format(result, expected))
    assert result == expected
    print("->test_deletion_distance_2: end")


def test():
    test_deletion_distance_1()
    print("======================")
    print("ALL TEST CASES FINISHED")


test()
