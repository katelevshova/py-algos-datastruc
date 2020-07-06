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


class QuickSort:
    def swap_numbers(self, input_list, lower_index: int, higher_index: int):
        if input_list[lower_index] != input_list[higher_index]:
            tmp: int = input_list[lower_index]
            input_list[lower_index] = input_list[higher_index]
            input_list[higher_index] = tmp
        print("->swap_numbers: "+str(input_list))

    def partition(self, input_list, low_index: int, high_index: int):
        index_lower = low_index - 1  # index of the smaller element
        pivot_element = input_list[high_index]

        for index in range(low_index, high_index):
            if input_list[index] <= pivot_element:
                index_lower += 1
                self.swap_numbers(input_list, index_lower, index)
        self.swap_numbers(input_list, index_lower+1, high_index)
        return index_lower+1

    def perform(self, input_list, low_index: int, high_index: int):
        if low_index < high_index:
            pivot_index = self.partition(input_list, low_index, high_index)
            self.perform(input_list, low_index, pivot_index - 1)
            self.perform(input_list, pivot_index + 1, high_index)


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
    print("->sort_list: input_list= "+str(input_list))
    quick_sort: QuickSort = QuickSort()
    quick_sort.perform(input_list, 0, len(input_list)-1)
    return input_list


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
