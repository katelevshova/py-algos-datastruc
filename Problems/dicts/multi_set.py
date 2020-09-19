class MultipleSet:
    def __init__(self):
        self.internal_dict = {}

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        if self.internal_dict.get(val):
            self.internal_dict[val] += 1
        else:
            self.internal_dict[val] = 1

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if self.internal_dict.get(val):
            if self.internal_dict.get(val) == 1:
                del self.internal_dict[val]
            else:
                self.internal_dict[val] -= 1

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if self.internal_dict.get(val):
            return True
        else:
            return False

    def __len__(self):
        # returns the number of elements in the multiset
        result_number = 0
        for key, value in self.internal_dict.items():
            result_number += value
        return result_number


def test_case_1():
    print("->test_case_1")
    """
    query 1
    add 1
    query 1
    remove 1
    query 1
    add 2
    add 2
    size
    query 2
    remove 2
    query 2
    size
    """

    multiset_1 = MultipleSet()
    print(1 in multiset_1)  # 1
    multiset_1.add(1)
    print(1 in multiset_1)  # 2
    multiset_1.remove(1)
    print(1 in multiset_1)  # 3
    multiset_1.add(2)
    multiset_1.add(2)
    print(len(multiset_1))  # 4
    print(2 in multiset_1)  # 5
    multiset_1.remove(2)
    print(2 in multiset_1)  # 6
    print(len(multiset_1))  # 7

    # Expected:
    """
    False   #1
    True    #2
    False   #3
    2       #4
    True    #5
    True    #6
    1       #7
    """


def test_case_2():
    print("->test_case_2")
    multiset_1 = MultipleSet()
    multiset_1.remove(1)


def test():
    test_case_1()
    test_case_2()


test()
