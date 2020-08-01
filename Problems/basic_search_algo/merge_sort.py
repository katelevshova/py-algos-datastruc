def perform_merge_sort(input_list) -> list:
    unit = 1
    while unit <= len(input_list):
        h = 0
        for h in range(0, len(input_list), unit * 2):
            l, r = h, min(len(input_list), h + 2 * unit)
            mid = h + unit
            # merge input_list[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                # use <= for stable merge merge
                if input_list[p] <= input_list[q]:
                    p += 1
                else:
                    tmp = input_list[q]
                    input_list[p + 1: q + 1] = input_list[p:q]
                    input_list[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2

    return input_list


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
