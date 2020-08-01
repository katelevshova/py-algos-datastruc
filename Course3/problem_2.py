"""
TASK2:
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and
your algorithm's runtime complexity must be in the order of O(log n).
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""


def rotated_array_search(input_list, target) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return search(input_list, target, 0, len(input_list) - 1)


def search(input_list: list, target: int, left_index: int, right_index: int) -> int:
    if right_index < left_index:
        return -1

    middle_index = (left_index + right_index) // 2
    if target == input_list[middle_index]:
        return middle_index  # Found element

    # The left or right half must be normally ordered. We need to find out which side and then use the normally
    # ordered half to figure out which side to search to find target.

    left_value = input_list[left_index]
    mid_value = input_list[middle_index]
    right_value = input_list[right_index]

    if left_value < mid_value:  # left is normally ordered
        if left_value <= target < mid_value:
            return search(input_list, target, left_index, middle_index - 1)  # search LEFT
        else:
            return search(input_list, target, middle_index + 1, right_index)  # search RIGHT
    elif left_value > mid_value:  # right is normally ordered
        if mid_value < target <= right_value:
            return search(input_list, target, middle_index + 1, right_index)  # search RIGHT
        else:
            return search(input_list, target, left_index, middle_index - 1)  # search LEFT
    elif left_value == mid_value:  # lef or right half is all repeats
        if mid_value != right_value:  # if right is different search it
            return search(input_list, target, middle_index + 1, right_index)  # search RIGHT
        else:  # search both halves
            result = search(input_list, target, left_index, middle_index - 1)  # search LEFT
            if result == -1:
                return search(input_list, target, middle_index + 1, right_index)  # search RIGHT
            else:
                return result
    return -1


def test_rotated_array_search_1():
    print("----------------------------------------")
    print("->test_rotated_array_search_1: start")
    result_actual = rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)
    result_expected = 0
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_1: end")


def test_rotated_array_search_2():
    print("----------------------------------------")
    print("->test_rotated_array_search_2: start")
    result_actual = rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)
    result_expected = 5
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_2: end")


def test_rotated_array_search_3():
    print("----------------------------------------")
    print("->test_rotated_array_search_3: start")
    result_actual = rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)
    result_expected = 2
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_3: end")


def test_rotated_array_search_4():
    print("----------------------------------------")
    print("->test_rotated_array_search_4: start")
    result_actual = rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)
    result_expected = 3
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_4: end")


def test_rotated_array_search_5():
    print("----------------------------------------")
    print("->test_rotated_array_search_5: start")
    result_actual = rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)
    result_expected = -1
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_5: end")


def test_rotated_array_search_6():
    print("----------------------------------------")
    print("->test_rotated_array_search_6: start")
    result_actual = rotated_array_search([7, 7, 7, 8, 9, 7], 9)
    result_expected = 4
    assert result_actual == result_expected, "result_expected = {}, result_actual = {}".format(result_expected,
                                                                                               result_actual)
    print("->test_rotated_array_search_6: end")


def test():
    test_rotated_array_search_1()
    test_rotated_array_search_2()
    test_rotated_array_search_3()
    test_rotated_array_search_4()
    test_rotated_array_search_5()
    test_rotated_array_search_6()


test()
