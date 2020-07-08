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
    '''
    NOTE:
    low_index - is a counter of zeroes in the input_list which counts from the beginning of the list, 
                the zeroes will be in range input_list[0:low_index] or starting from 0 and ending at low_index-1
    mid_index - is a counter of ones in input_list which counts from the beginning of the list,  
                the ones will be in range input_list[low_index:mid_index] or starting from low_index to mid_index-1
    Since we don't know the range between ones and 2s we count high_index from the end of the input_list.
    high_index - is a counter for 2s in the input_list from the end, we continue until high_index meets the mid_index
    '''

    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            # swap low and middle
            swap_numbers(input_list, low_index, mid_index)
            # increment low and middle indexes
            low_index += 1
            mid_index += 1
        elif input_list[mid_index] == 1:
            # increment only middle index
            mid_index += 1
        elif input_list[mid_index] == 2:
            # swap middle and high
            swap_numbers(input_list, mid_index, high_index)
            # decrement high
            high_index -= 1
        else:
            return []

    return input_list


def swap_numbers(input_list, lower_index: int, higher_index: int):
    if input_list[lower_index] != input_list[higher_index]:  # optimization: swap only if different
        input_list[lower_index], input_list[higher_index] = input_list[higher_index], input_list[lower_index]
    # print("->swap_numbers: "+str(input_list))


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
