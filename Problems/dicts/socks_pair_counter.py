"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of
socks with matching colors there are.

Function Description

It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
"""


def sockMerchant(n, ar) -> int:
    socks_dict = {}
    result_counter = 0

    for item in ar:
        if socks_dict.get(item):
            socks_dict[item] += 1
        else:
            socks_dict[item] = 1

        if socks_dict[item] % 2 == 0:
            result_counter += 1

    print(socks_dict)
    print(result_counter)

    return result_counter


def test_1():
    print("->test_1")
    actual_result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    expected_result = 3
    assert actual_result == expected_result


def test_2():
    print("->test_2")
    actual_result = sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
    expected_result = 4
    assert actual_result == expected_result


def test():
    test_1()
    test_2()


test()
