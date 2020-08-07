def sum(str1: str, str2: str) -> str:
    """
    Find the sum of two numbers represented as strings.
    Args:
        str1 - string: number
        str2 - string: number

    Returns - string: The result sum
    """

    print("str1=" + str(str1) + ", str2=" + str(str2))

    if not str1.isdigit() or not str2.isdigit() or str1 is None or str2 is None:
        return None

    list1 = list(str1)
    list2 = list(str2)
    print("list1=" + str(list1))
    print("list2=" + str(list2))
    result_str = ""

    if len(str1) > len(str2):
        smaller_number = str2
        larger_number = str1
    else:
        smaller_number = str1
        larger_number = str2

    larger_index = len(larger_number) - 1

    digit_in_memory = 0

    for index in range(len(smaller_number), 0, -1):
        digit1 = int(smaller_number[index - 1])
        digit2 = int(larger_number[larger_index])

        cur_sum = digit1 + digit2 + digit_in_memory

        if cur_sum > 9:
            result_str += str(cur_sum)[-1]
            digit_in_memory = int(str(cur_sum)[0])
        else:
            result_str += str(cur_sum)
            digit_in_memory = 0

        if index == 1 and digit_in_memory != 0:
            if len(str1) == len(str2):
                result_str += str(digit_in_memory)
            else:
                cur_sum = int(larger_number[larger_index - 1]) + digit_in_memory
                result_str += str(cur_sum)

        larger_index -= 1

    reverse_result = result_str[::-1]
    first_part = ""

    if len(str1) != len(str2):
        first_part = larger_number[0:len(larger_number) - len(reverse_result):1]
    result_number = first_part + reverse_result

    return result_number


def test_case_1():
    print("\n->test_case_1")
    actual_result = sum("198", "13")
    expected = "211"
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case1", actual_result, expected)


def test_case_2():
    print("\n->test_case_2")
    actual_result = sum("100000000000008", "94563")
    expected = "100000000094571"
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case2", actual_result, expected)


def test_case_3():
    print("\n->test_case_3")
    actual_result = sum("35989", "94563")
    expected = "130552"
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case3", actual_result, expected)


def test_case_4():
    print("\n->test_case_4")
    actual_result = sum("100098", "99")
    expected = "100197"
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case4", actual_result, expected)


def test_case_5():
    print("\n->test_case_5")
    actual_result = sum("fdf45", "df99")
    expected = None
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case5", actual_result, expected)


def test_case_6():
    print("\n->test_case_6")
    actual_result = sum("", None)
    expected = None
    print("actual_result={}, expected={}".format(actual_result, expected))
    assert actual_result == expected, "{}, actual_result={}, expected={}".format("case6", actual_result, expected)


def test():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    print("================================")
    print("ALL TESTS ARE FINISHED")


test()
