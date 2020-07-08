"""
TASK4:
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.
Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice,
that would still be an O(n) solution but it will not count as single traversal.
"""


def sort_012(input_list) -> list:
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) == 0:
        return []

    low_index = mid_index = 0
    high_index = len(input_list) - 1

    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            # swap low and middle
            input_list[low_index], input_list[mid_index] = input_list[mid_index], input_list[low_index]
            # increment low and middle indexes
            low_index += 1
            mid_index += 1
        elif input_list[mid_index] == 1:
            # increment only middle index
            mid_index += 1
        elif input_list[mid_index] == 2:
            # swap middle and high
            input_list[mid_index], input_list[high_index] = input_list[high_index], input_list[mid_index]
            # decrement high
            high_index -= 1
        else:
            return []

    return input_list


def test():
    test_list = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    actual_result = sort_012(test_list)
    expected_result = sorted(test_list)
    print("case1: \n" + str(actual_result))
    assert actual_result == expected_result, "{}, actual={}, expected={}".format("case1", actual_result,
                                                                                 expected_result)

    test_list = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    actual_result = sort_012(test_list)
    expected_result = sorted(test_list)
    print("case2: \n" + str(actual_result))
    assert actual_result == expected_result, "{}, actual={}, expected={}".format("case2", actual_result,
                                                                                 expected_result)

    test_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    actual_result = sort_012(test_list)
    expected_result = sorted(test_list)
    print("case3: \n" + str(actual_result))
    assert actual_result == expected_result, "{}, actual={}, expected={}".format("case3", actual_result,
                                                                                 expected_result)

    actual_result = sort_012([])
    print("case4: \n" + str(actual_result))
    assert actual_result == [], "{}, actual={}, expected={}".format("case4", actual_result,
                                                                    expected_result)

    test_list = [-1, -2, 0, 2, 3]
    actual_result = sort_012(test_list)
    expected_result = []
    print("case5: \n" + str(actual_result))
    assert actual_result == expected_result, "{}, actual={}, expected={}".format("case5", actual_result,
                                                                                 expected_result)

    test_list = [0, 0, 0, 0, 0, None, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, -2]
    actual_result = sort_012(test_list)
    expected_result = []
    print("case6: \n" + str(actual_result))
    assert actual_result == expected_result, "{}, actual={}, expected={}".format("case6", actual_result,
                                                                                 expected_result)


test()
