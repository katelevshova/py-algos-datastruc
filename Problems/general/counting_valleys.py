"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small
details like topography. During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U , or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down represents a 1
unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a
step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting
with a step down from sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike,
find and print the number of valleys he walked through.

For example, if Gary's path is s = "DDUUUUDD", he first enters a valley 2 units deep.
Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below.
It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

    n: the number of steps Gary takes
    s: a string describing his path


"""


def countingValleys(n, s) -> int:
    level = 0
    valleys_number = 0

    for char in s:
        if char == "U":
            level += 1
            if level == 0:
                valleys_number += 1
        else:
            level -= 1
    return valleys_number


def test_1():
    print("->test_1")
    actual_result = countingValleys(8, "UDDDUDUU")
    """
    _/\      _
       \    /
        \/\/
    """
    expected_result = 1
    assert actual_result == expected_result


def test_2():
    print("->test_2")
    actual_result = countingValleys(8, "DDUUUUDD")
    expected_result = 1
    assert actual_result == expected_result


def test_3():
    print("->test_3")
    actual_result = countingValleys(10, "DDUUUUDDDU")
    expected_result = 2
    assert actual_result == expected_result


def test_4():
    print("->test_4")
    actual_result = countingValleys(12, "DDUUDDUDUUUD")
    expected_result = 2
    assert actual_result == expected_result


def test():
    test_1()
    test_2()
    test_3()
    test_4()


test()
