def sort_dict_by_key_value():
    key_value = {}
    key_value["b"] = 56
    key_value["a"] = 2
    key_value["d"] = 12
    key_value["c"] = 24
    key_value["f"] = 18
    key_value["e"] = 323

    # example1 - sort by key
    print(sorted(key_value.items(), key=lambda kv: (kv[0], kv[1])))  # key, value
    # example2 - printing on each line and sort by key
    for i, value in sorted(key_value.items()):
        print((i, value), end="\n")
    # example3 - sort by value
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))  # value, key

    # printed sorted keys only
    print(sorted(key_value.keys()))

    # printed sorted values only
    print(sorted(key_value.values()))


sort_dict_by_key_value()
