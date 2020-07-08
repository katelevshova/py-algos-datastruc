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
        # print("->swap_numbers: "+str(input_list))

    def partition(self, input_list, low_index: int, high_index: int):
        index_lower = low_index - 1  # index of the smaller element
        pivot_element = input_list[high_index]

        if pivot_element is None:
            raise ValueError("Pivot element is None")

        for index in range(low_index, high_index):
            if input_list[index] is None:
                raise ValueError("Element with index={} is None".format(index))

            if input_list[index] <= pivot_element:
                index_lower += 1
                self.swap_numbers(input_list, index_lower, index)
        self.swap_numbers(input_list, index_lower + 1, high_index)
        return index_lower + 1

    def perform(self, input_list, low_index: int, high_index: int):
        if low_index < high_index:
            pivot_index = self.partition(input_list, low_index, high_index)
            self.perform(input_list, low_index, pivot_index - 1)
            self.perform(input_list, pivot_index + 1, high_index)


def rearrange_digits(input_list) -> list:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # sort the list
    sorted_list = sort_list(input_list)
    print("->rearrange_digits:")
    first_number_str = ""
    second_number_str = ""

    for i in range(len(sorted_list) - 1, -1, -1):
        if i % 2 == 0:  # even position
            first_number_str += str(sorted_list[i])
        else:
            second_number_str += str(sorted_list[i])
    print("first_number_str= " + first_number_str + ", second_number_str= " + second_number_str)
    if first_number_str > second_number_str:
        return [int(first_number_str), int(second_number_str)]
    else:
        return [int(second_number_str), int(first_number_str)]


def sort_list(input_list) -> list:
    print("->sort_list: input_list= " + str(input_list))
    quick_sort: QuickSort = QuickSort()
    quick_sort.perform(input_list, 0, len(input_list) - 1)
    print("->sort_list: result= " + str(input_list))
    return input_list


def test():
    test_sort_list_1()
    test_sort_list_2()
    # test_sort_list_3()
    test_sort_list_4()
    test_rearrange_digits_1()
    test_rearrange_digits_2()
    test_rearrange_digits_3()



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
    expected_result = [531, 42]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_rearrange_digits_2: end")


def test_rearrange_digits_3():
    print("---------------------------------")
    print("->test_rearrange_digits_3: start")
    actual_result = rearrange_digits([4, 9, 2, 5, 9, 8])  # 2,4,5,8,9,9
    expected_result = [984, 952]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_rearrange_digits_3: end")


def test_sort_list_1():
    print("---------------------------------")
    print("->test_sort_list_1: start")
    actual_result = sort_list([4, 6, 2, 5, 9, 8])
    expected_result = [2, 4, 5, 6, 8, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_1: end")


def test_sort_list_2():
    print("---------------------------------")
    print("->test_sort_list_2: start")
    actual_result = sort_list([4, 6, 0, 2, 5, 9, 9, 8])
    expected_result = [0, 2, 4, 5, 6, 8, 9, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_2: end")


def test_sort_list_3():
    print("---------------------------------")
    print("->test_sort_list_3: start")
    sort_list([4, 6, None, 2, 5, 9, None, 8])
    print("->test_sort_list_3: end")


def test_sort_list_4():
    print("---------------------------------")
    print("->test_sort_list_4: start")
    actual_result = sort_list([4, 6, 0, 2, 5, 9, 1, 3])
    expected_result = [0, 1, 2, 3, 4, 5, 6, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_4: end")


test()
