def mostActive(customers):
    cursomers_dict = {}
    total_trades = len(customers)

    for item in customers:
        if cursomers_dict.get(item):
            cursomers_dict[item][0] += 1
            cursomers_dict[item][1] = (100 * cursomers_dict[item][0]) / total_trades
        else:
            cursomers_dict[item] = [1, 100 / total_trades]

    print(cursomers_dict)
    sorted_dict = dict(sorted(cursomers_dict.items(), key=lambda item: item[0])) # by key

    print("---------")
    print(sorted_dict)

    result = []
    for key, value in sorted_dict.items():
        print(key, value)
        if value[1] >= 5:
            result.append(key)
    print(result)
    return result


"""
from sortedcontainers import SortedDict
def mostActive(customers):
    # Write your code here

    cursomers_dict = SortedDict()
    total_trades = len(customers)

    for item in customers:
        if cursomers_dict.get(item):
            cursomers_dict[item][0] += 1
            cursomers_dict[item][1] = (100 * cursomers_dict[item][0]) / total_trades
        else:
            cursomers_dict[item] = [1, 100/total_trades]

    print(cursomers_dict)

    result = []
    for key, value in cursomers_dict.items():
        print(key, value)
        if value[1] >= 5:
            result.append(key)
    print(result)
    return result
"""


def test_case_1():
    print("->test_case_1")
    actual_result = mostActive(
        ["a", "o", "b", "a", "a", "a", "a", "a", "a", "a", "a", "o", "b", "a", "a", "a", "a", "a", "a", "a", "o", "b",
         "b", "b", "b", "b", "b", "g"])
    expected_result = ["a", "b", "o"]
    assert actual_result == expected_result, "actual_result={}, expected_result={}".format(str(actual_result),
                                                                                          str(expected_result))


def test():
    test_case_1()


test()
