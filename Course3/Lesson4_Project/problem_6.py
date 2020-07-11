"""
TASK6:
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
Sorting usually requires O(n log n) time. Can you come up with a O(n) algorithm (i.e., linear time)?
"""
import random


def get_min_max(input_list: list) -> tuple:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       input_list(list): list of integers containing one or more integers
    """
    print("->get_min_max: input_list= " + str(input_list))

    if len(input_list) < 2:
        raise ValueError("input_list must be initialized with at least 2 elements!")

    min_value: int = input_list[0]
    max_value: int = input_list[1]

    for i in range(2, len(input_list)):
        current_value = input_list[i]
        print("i="+str(i)+", current_value="+str(current_value))

    return min_value, max_value

    pass


def test_get_min_max_1():
    print("-----------------------------------")
    print("->test_get_min_max_1:start ")
    actual_result = get_min_max([8, 2, 9, 1, 3, 6, 4, 0, 5, 7])
    expected_result = (0, 9)
    assert actual_result == expected_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_get_min_max_1:end ")


def test():
    test_get_min_max_1()


test()