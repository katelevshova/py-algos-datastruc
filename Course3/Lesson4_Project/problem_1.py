"""
TASK1:
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    print("->sqrt for number " + str(number))

    if number == 0 or number is None:
        return 0

    if number == 1:
        return 1

    counter = 2

    while True:
        square = counter * counter
        print("counter= " + str(counter) + ", square=" + str(square))

        if square < number:
            counter += 1
        else:
            return counter


def test_sqrt():
    print("----------------------------------------------------------------------------------")
    # case1
    expected_result = 3
    actual_result = sqrt(9)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case1: ", expected_result,
                                                                                       actual_result)
    print("----------------------------------------------------------------------------------")
    # case2
    expected_result = 0
    actual_result = sqrt(0)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case2: ", expected_result,
                                                                                       actual_result)
    print("----------------------------------------------------------------------------------")
    # case3
    expected_result = 4
    actual_result = sqrt(16)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case3: ", expected_result,
                                                                                       actual_result)
    print("----------------------------------------------------------------------------------")
    # case4
    expected_result = 1
    actual_result = sqrt(1)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case4: ", expected_result,
                                                                                       actual_result)
    print("----------------------------------------------------------------------------------")
    # case5
    expected_result = 5
    actual_result = sqrt(27)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case5: ", expected_result,
                                                                                       actual_result)
    print("----------------------------------------------------------------------------------")
    # case6
    expected_result = 0
    actual_result = sqrt(None)
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case6: ", expected_result,
                                                                                       actual_result)


test_sqrt()
