def topCompetitors(topN, competitors, reviews):
    comp_rev_dict = {}
    print("competitors=" + str(competitors) + "\n")

    for comp_name in competitors:
        for review in reviews:
            count = review.find(comp_name)
            if count == -1:
                count = 0
            else:
                count = 1

            if comp_rev_dict.get(comp_name) is None:
                comp_rev_dict[comp_name] = count
            else:
                comp_rev_dict[comp_name] += count

    print("created comp_rev_dict= ")
    print(comp_rev_dict)

    # NOTE: this won't sort keys with the same value alphabetically ASC
    #sorted_by_value_dict_1 = dict(sorted(comp_rev_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
    #print("\nsorted by VALUE, DESC")
    #print(sorted_by_value_dict_1)

    print("\nsorted by VALUE, DESC and by KEYS alphabetically ASC")
    sorted_by_value_dict = dict(sorted(comp_rev_dict.items(), key=lambda kv: (-kv[1], kv[0])))
    print(sorted_by_value_dict)

    result_names_list = list(sorted_by_value_dict.keys())

    print("\nresult_names_list=")

    if topN < len(result_names_list):
        print(result_names_list[0:topN])
        return result_names_list[0:topN]
    else:
        print(str(result_names_list))
        return result_names_list


def test_case1():
    print("\n->test_case1: start")

    test_comp = ["anabell", "betalar", "cecular", "delcecular", "eurgel"]
    rev = ["Best by anabell", "betalar has great", "anabell provide"]
    actual_result = topCompetitors(2, test_comp, rev)
    expected_result = ["anabell", "betalar"]
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case1: end")


def test_case2():
    print("\n->test_case2: start")

    test_comp = ["bartt", "betalar", "anabell", "cecular", "delcecular", "eurgel"]
    rev = ["anabell Best by bartt", "betalar has great", " betalar provide"]
    actual_result = topCompetitors(2, test_comp, rev)
    expected_result = ["betalar", "anabell"]
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case2: end")


def test_case3():  # NOT anabell 2 times in 1 review
    print("\n->test_case3: start")

    test_comp = ["bartt", "betalar", "anabell", "cecular", "delcecular", "eurgel"]
    rev = ["anabell Best by anabell bartt anabell", "betalar has great", " betalar prvocide"]
    actual_result = topCompetitors(2, test_comp, rev)
    expected_result = ["betalar", "anabell"]
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case3: end")


def test_case4():  # topN > length of competitors
    print("\n->test_case4: start")

    test_comp = ["bartt", "betalar", "anabell", "cecular", "delcecular", "eurgel"]
    rev = ["anabell Best by anabell bartt", "betalar has great", " betalar prvocide"]
    actual_result = topCompetitors(999, test_comp, rev)
    expected_result = ["betalar", "anabell", "bartt", 'cecular', 'delcecular', 'eurgel']
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case4: end")


def test_case5():  # topN = length of competitors
    print("\n->test_case5: start")

    test_comp = ["bartt", "betalar", "anabell", "cecular", "delcecular", "eurgel"]
    rev = ["anabell Best by anabell bartt", "betalar has great", " betalar prvocide"]
    actual_result = topCompetitors(6, test_comp, rev)
    expected_result = ["betalar", "anabell", "bartt", 'cecular', 'delcecular', 'eurgel']
    assert actual_result == expected_result, "actual={}, expected={}".format(actual_result, expected_result)
    print("->test_case5: end")


def test():
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    print("=====================")
    print("ALL TESTS FINISHED")


test()
