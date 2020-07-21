def perform_merge_sort(input_list) -> list:
    if len(input_list) <= 1:
        return input_list

    mid_index = len(input_list) // 2  # finding the middle of the arr
    left_part = input_list[:mid_index]
    right_part = input_list[mid_index:]

    left_part = perform_merge_sort(left_part)
    right_part = perform_merge_sort(right_part)

    return merge(left_part, right_part)


def merge(left_part, right_part) -> list:
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] < right_part[right_index]:
            merged_list.append(left_part[left_index])
            left_index += 1
        else:
            merged_list.append(right_part[right_index])
            right_index += 1

    merged_list += left_part[left_index:]
    merged_list += right_part[right_index:]

    return merged_list


def test_sort_list_1():
    print("---------------------------------")
    print("->test_sort_list_1: start")
    test_list = [4, 6, 2, 5, 9, 8]
    print(str(test_list))
    actual_result = perform_merge_sort(test_list)
    print(str(actual_result))
    expected_result = [2, 4, 5, 6, 8, 9]

    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_1: end")


def test_sort_list_2():
    print("---------------------------------")
    print("->test_sort_list_2: start")
    test_list = [4, 6, 0, 2, 5, 9, 9, 8]
    print(str(test_list))
    actual_result = perform_merge_sort(test_list)
    print(str(actual_result))
    expected_result = [0, 2, 4, 5, 6, 8, 9, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_2: end")


def test_sort_list_3():
    print("---------------------------------")
    print("->test_sort_list_3: start")
    perform_merge_sort([4, 6, None, 2, 5, 9, None, 8])
    print("->test_sort_list_3: end")


def test_sort_list_4():
    print("---------------------------------")
    print("->test_sort_list_4: start")
    test_list = [4, 6, 0, 2, 5, 9, 1, 3]
    print(str(test_list))
    actual_result = perform_merge_sort(test_list)
    print(str(actual_result))
    expected_result = [0, 1, 2, 3, 4, 5, 6, 9]
    assert expected_result == actual_result, "expected is {}, actual is {}".format(expected_result, actual_result)
    print("->test_sort_list_4: end")


def test():
    print("TEST CASES FOR SORTING")
    test_sort_list_1()
    test_sort_list_2()
    # test_sort_list_3()
    test_sort_list_4()


test()
