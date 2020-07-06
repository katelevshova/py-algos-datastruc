"""
TASK3:
Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers
cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the
expected time complexity is O(nlog(n)).
for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # sort the list

    print("->rearrange_digits: input_list= ")


def sort_list(input_list) -> list:
    return


def test():
    test_sort_list()


def test_rearrange_digits_1():
    print("---------------------------------")
    print("->test_rearrange_digits_1: start")
    actual_result = rearrange_digits([4, 6, 2, 5, 9, 8])
    expected_result = [964, 852]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_rearrange_digits_1: end")


def test_rearrange_digits_2():
    print("---------------------------------")
    print("->test_rearrange_digits_2: start")
    actual_result = rearrange_digits([1, 2, 3, 4, 5])
    expected_result = [542, 31]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_rearrange_digits_2: end")


def test_rearrange_digits_3():
    print("---------------------------------")
    print("->test_rearrange_digits_3: start")
    actual_result = rearrange_digits([1, 2, 3, 4, 5])
    expected_result = [531, 42]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_rearrange_digits_3: end")


def test_sort_list():
    print("---------------------------------")
    print("->test_sort_list: start")
    actual_result = sort_list([4, 6, 2, 5, 9, 8])
    expected_result = [2, 4, 5, 6, 8, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list: end")


test()
