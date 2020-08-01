"""
 Write a function that implements the binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found

"""


def binary_search(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2  # integer division
        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index
        elif target < mid_element:  # we will search only in the left half
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1  # we will search only in the right half
    return -1
    pass


def test_binary_search(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("->test_binary_search: Pass!")
    else:
        print("->test_binary_search: Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_binary_search(test_case)

"""Write a function that implements the binary search algorithm using recursion

   args:
     array: a sorted array of items of the same type
     target: the element you're searching for

   returns:
     int: the index of the target, if found, in the source
     -1: if the target is not found
"""


def binary_search_recursive(array, target):
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)
    pass


def binary_search_recursive_soln(array, target: int, start_index: int, end_index: int):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2

    if target == array[mid_index]:
        return mid_index
    elif target < array[mid_index]:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


def test_binary_search_recursive(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("->test_binary_search_recursive: Pass!")
    else:
        print("->test_binary_search_recursive: Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4
index = 4
test_case = [array, target, index]
test_binary_search_recursive(test_case)
