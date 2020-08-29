def balanced_partition(parent, files_size) -> int:
    print("parent= " + str(parent))
    print("files_size= " + str(files_size))

    # get index of 1st 0

    separator_index = parent[1]

    subs_number = 0
    for i in parent:
        if i == 0:
            subs_number += 1
    print("subs_number=" + str(subs_number))
    sub_dict = {}

    for j in range(1, subs_number + 1):
        if sub_dict.get(j) is None:
            sub_dict[j] = []

    print("sub_dict=" + str(sub_dict))


    for key in sub_dict:
        print("key=" + str(key))
        for i in range(0, len(parent)):
            print("i=" + str(i) + ", parent[" + str(i) + "]=" + str(parent[i]))
            if parent[i] == key or i == key:  # index of first child of root
                file_size_value = files_size[i]
                print("file_size_value=" + str(file_size_value))
                sub_dict[key].append(file_size_value)
                print("sub_dict[" + str(key) + "]=" + str(sub_dict[key]))

    sub_dict[subs_number].append(files_size[0]) # add root value

    print("sub_dict=" + str(sub_dict))


    return 0


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
    # test_case_2()
    # test_case_3()
    print("=====================")
    print("ALL TESTS FINISHED")


test()
