"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
Given an integer,n, find and print the number of letter a's in the first
letters of Lilah's infinite string.

For example, if the string s = "abcac" and n=10, the substring we consider is abcacabcac,
the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.
It should return an integer representing the number of occurrences of a in the prefix of length n
in the infinitely repeating string.

repeatedString has the following parameter(s):
    s: a string to repeat
    n: the number of characters to consider
"""


def repeatedString(s, n) -> int:
    chars_number = 0
    current_len = len(s)

    if current_len == 1 and s == "a":
        return n
    current_a_number = s.count("a")

    if current_a_number == 0:
        return 0

    whole_parts = n // current_len
    a_in_whole_parts = whole_parts * current_a_number

    leftover = n % current_len
    new_str = s[0:leftover]
    chars_number = a_in_whole_parts + new_str.count("a")

    return chars_number


def test_case_1():
    print("->test_case_1")
    actual_result = repeatedString("abcac", 10)  # abcacabcac
    expected_result = 4
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_2():
    print("->test_case_2")
    actual_result = repeatedString("aba", 10)
    expected_result = 7
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_3():
    print("->test_case_3")
    actual_result = repeatedString("a", 1000000000000)
    expected_result = 1000000000000
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_4():
    print("->test_case_4")
    actual_result = repeatedString("abcdefa", 2)
    expected_result = 1
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_5():
    print("->test_case_5")
    actual_result = repeatedString("aacdefa", 2)
    expected_result = 2
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_6():
    print("->test_case_6")
    actual_result = repeatedString("fhfhfh", 2)
    expected_result = 0
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_7():
    print("->test_case_7")
    actual_result = repeatedString("b", 1000000000000)
    expected_result = 0
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test_case_8():
    print("->test_case_8")
    actual_result = repeatedString("", 1000000000000)
    expected_result = 0
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                           str(expected_result))


def test():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    test_case_8()
    print("ALL TESTS FINISHED...")


test()
