"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the
number of the current cloud plus 1 or 2.
She must avoid the thunderheads. Determine the minimum number of jumps it will take
Emma to jump from her starting position to the last cloud.
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1
if they must be avoided.
For example, c=[0,1,0,0,0,1,0] indexed from 0...6. The number on each cloud is its
 index in the list so she must avoid the clouds at indexes 1 and 5.
 She could follow the following two paths:
0 -> 2 -> 4 -> 6
or
0 -> 2 -> 3 -> 4 -> 6
The first path takes 3 jumps while the second takes 4.

Function Description

Complete the jumpingOnClouds function in the editor below.
It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):
    c: an array of binary integers

"""


def jumping_on_clouds(c) -> int:
    jumps_counter = 0
    current_pos = 0

    if len(c) == 2 and 0 in c:
        return 1

    while current_pos < len(c):
        if current_pos + 2 < len(c) and c[current_pos + 2] == 0:
            current_pos += 2
            jumps_counter += 1
        elif current_pos + 1 < len(c) and c[current_pos + 1] == 0:
            current_pos += 1
            jumps_counter += 1
        else:
            current_pos += 1

    return jumps_counter


def test_1():
    print("->test_1:start")
    actual_result = jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    expected_result = 4
    assert actual_result == expected_result
    print("->test_1:end")


def test_2():
    print("->test_2: start")
    actual_result = jumping_on_clouds([0, 1, 0, 0, 0, 1, 0])
    expected_result = 3
    assert actual_result == expected_result
    print("->test_2: end")


def test_3():
    print("->test_3: start")
    actual_result = jumping_on_clouds([1, 1])
    expected_result = 0
    assert actual_result == expected_result
    print("->test_3: end")


def test_4():
    print("->test_4:start")
    actual_result = jumping_on_clouds([1, 0])
    expected_result = 1
    assert actual_result == expected_result, "case4_1"

    actual_result = jumping_on_clouds([0, 1])
    expected_result = 1
    assert actual_result == expected_result, "case4_2"

    actual_result = jumping_on_clouds([0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1])
    expected_result = 1
    assert actual_result == expected_result, "case4_3"
    print("->test_4: end")


def test_5():
    print("->test_5: start")
    actual_result = jumping_on_clouds([0, 0, 0, 1, 0, 0])
    expected_result = 3
    assert actual_result == expected_result
    print("->test_5: end")


def test():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("ALL TESTS FINISHED...")


test()
