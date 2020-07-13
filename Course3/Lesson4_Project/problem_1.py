"""
TASK1:
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))
"""


def sqrt(number) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    print("->sqrt for number " + str(number))
    if number == 0:
        return 0

    if number is None or number < 0:
        return "Error"

    if number == 1:
        return 1

    counter = 2

    while True:
        square = counter * counter
        print("counter= " + str(counter) + ", square=" + str(square))

        if square == number:
            return counter
        elif square < number:
            counter += 1
        else:
            return counter - 1


def test_sqrt():
    print("case1----------------------------------------------------------------------------------")
    # case1
    expected_result = 3
    actual_result = sqrt(9)
    print("result= "+str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case1: ", expected_result,
                                                                                       actual_result)
    print("\ncase2----------------------------------------------------------------------------------")
    # case2
    expected_result = 0
    actual_result = sqrt(0)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case2: ", expected_result,
                                                                                       actual_result)
    print("\ncase3----------------------------------------------------------------------------------")
    # case3
    expected_result = 4
    actual_result = sqrt(16)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case3: ", expected_result,
                                                                                       actual_result)
    print("\ncase4----------------------------------------------------------------------------------")
    # case4
    expected_result = 1
    actual_result = sqrt(1)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case4: ", expected_result,
                                                                                       actual_result)
    print("\ncase5----------------------------------------------------------------------------------")
    # case5
    expected_result = 5
    actual_result = sqrt(27)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case5: ", expected_result,
                                                                                       actual_result)
    print("\ncase6----------------------------------------------------------------------------------")
    # case6
    expected_result = 5
    actual_result = sqrt(34)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case6: ", expected_result,
                                                                                       actual_result)
    print("\ncase7----------------------------------------------------------------------------------")
    # case7
    expected_result = "Error"
    actual_result = sqrt(None)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case7: ", expected_result,
                                                                                       actual_result)
    print("\ncase8----------------------------------------------------------------------------------")
    # case8
    expected_result = "Error"
    actual_result = sqrt(-16)
    print("result= " + str(actual_result))
    assert (expected_result == actual_result), "{}expected is {}, actual is {}".format("case8: ", expected_result,
                                                                                       actual_result)


test_sqrt()
