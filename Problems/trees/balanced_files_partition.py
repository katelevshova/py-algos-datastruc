"""
Given a set of integers, the task is to divide it into
two sets S1 and S2 such that the absolute difference between their sums is minimum.

If there is a set S with n elements,
then if we assume Subset1 has m elements,
Subset2 must have n-m elements and
the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

"""
import sys

class NonBinTree:

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def __repr__(self):
        return f"NonBinTree({self.val}): {self.nodes}"

def balanced_partition(parent, files_size) -> int:
    print("parent= " + str(parent))
    print("files_size= " + str(files_size))

    #split on 2 halfs
    # calculate sum of each half
    # save the absolute difference between them
    # find the minimum

    sum = 0
    n = len(files_size)

    #calculate sum of all elements
    for i in range (n):
        sum += files_size[i]

    print("sum="+str(sum))

    # Create an 2d list to store results of subproblems
    table = [[0 for i in range(sum + 1)]
          for j in range(n + 1)]

    print(*table, sep="\n")
    print("---------------------------------")

    """
    Initialize first column as true.
    0 sum is possible with all elements.
    """
    for i in range(n + 1):
        table[i][0] = True

    print(*table, sep="\n")

    print("---------------------------------")
    """
    Initialize top row, except table[0][0] as false. 
    With 0 elements, no other sum except 0 is possible
    """
    for j in range(1, sum + 1):
        table[0][j] = False

    print(*table, sep="\n")

    print("---------------------------------")

    # Fill the partition table in
    # bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):

            # If i'th element is excluded
            table[i][j] = table[i - 1][j]

            # If i'th element is included
            if files_size[i - 1] <= j:
                table[i][j] |= table[i - 1][j - files_size[i - 1]]

    print(*table, sep="\n")

    print("---------------------------------")

    # Initialize difference
    # of two sums.
    diff = sys.maxsize

    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(sum // 2, -1, -1):
        if table[n][j] == True:
            diff = sum - (2 * j)
            break



    return diff




def test_case_1():
    print("->test_case_1:start")
    test_parent = [-1, 0, 0, 1, 1, 2]
    test_files_size = [1, 2, 2, 1, 1, 1]
    actual_result = balanced_partition(test_parent, test_files_size)
    expected_result = 0
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case_1:end")


def test_case_2():
    print("->test_case_2:start")
    test_parent = [-1, 0, 1, 2]
    test_files_size = [1, 4, 3, 4]
    # {0,1} with size 1+4 =5, {2,3} with size 3+4=7. |5-7|=2 is minimum
    actual_result = balanced_partition(test_parent, test_files_size)
    expected_result = 2
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case_2:end")


def test_case_3():
    print("->test_case_3:start")
    test_parent = [-1, 0, 0, 0]
    test_files_size = [10, 11, 10, 10]
    # {0,2,3} with 10+10+10=30 and {1} with 11. The absolute difference between sizes is |30-11|=19
    actual_result = balanced_partition(test_parent, test_files_size)
    expected_result = 19
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case_3:end")


def test():
    test_case_1()
    test_case_2()
    test_case_3()
    print("=====================")
    print("ALL TESTS FINISHED")


test()
