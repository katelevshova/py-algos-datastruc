"""
TASK6:
Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
Sorting usually requires O(n log n) time. Can you come up with a O(n) algorithm (i.e., linear time)?
"""


def get_min_max(input_list: list) -> tuple:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       input_list(list): list of integers containing one or more integers
    """
    print("->get_min_max: input_list= " + str(input_list))

    if len(input_list) < 2:
        # raise ValueError("input_list must be initialized with at least 2 elements!")
        print("input_list must be initialized with at least 2 elements!")
        return None, None

    if input_list[0] is None or input_list[1] is None:
        print("input_list must not contain None values!")
        return None, None

    if input_list[0] < input_list[1]:
        min_value = input_list[0]
        max_value = input_list[1]
    else:
        min_value = input_list[1]
        max_value = input_list[0]

    # print("init: min_value="+str(min_value)+", max_value= "+str(max_value))

    for i in range(2, len(input_list)):
        current_value = input_list[i]

        if current_value is None:
            print("input_list must not contain None values!")
            return None, None

        # print("i="+str(i)+", current_value="+str(current_value))
        if current_value < min_value:
            min_value = current_value
        if current_value > max_value:
            max_value = current_value
        # print("min_value=" + str(min_value) + ", max_value= " + str(max_value))

    result = min_value, max_value
    print("result= " + str(result))
    return result


def test_get_min_max_1():
    print("-----------------------------------")
    print("->test_get_min_max_1:start ")
    actual_result = get_min_max([8, 2, 9, 1, 3, 6, 4, 0, 5, 7])
    expected_result = (0, 9)
    assert actual_result == expected_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_get_min_max_1:end ")


def test_get_min_max_2():
    print("-----------------------------------")
    print("->test_get_min_max_2:start ")
    assert get_min_max([2]) == (None, None)
    assert get_min_max([]) == (None, None)
    print("->test_get_min_max_2:end ")


def test_get_min_max_3():
    print("-----------------------------------")
    print("->test_get_min_max_3:start ")
    assert get_min_max([78, 1]) == (1, 78)
    print("->test_get_min_max_3:end ")


def test_get_min_max_4():
    print("-----------------------------------")
    print("->test_get_min_max_4:start ")
    actual_result = get_min_max([8, 2, 9, None, 3, 6, 4, 0, 5, 7])
    expected_result = (None, None)
    assert actual_result == expected_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_get_min_max_4:end ")


def test_get_min_max_5():
    print("-----------------------------------")
    print("->test_get_min_max_5:start ")
    assert get_min_max([None, 1]) == (None, None)
    print("->test_get_min_max_5:end ")


def test_get_min_max_6():
    print("-----------------------------------")
    print("->test_get_min_max_6:start ")
    actual_result = get_min_max([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    expected_result = (0, 9)
    assert actual_result == expected_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_get_min_max_6:end ")


def test():
    test_get_min_max_1()
    test_get_min_max_2()
    test_get_min_max_3()
    test_get_min_max_4()
    test_get_min_max_5()
    test_get_min_max_6()


test()
