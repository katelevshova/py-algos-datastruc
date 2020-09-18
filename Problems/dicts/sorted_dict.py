def sort_dict_by_key_value():
    key_value = {}
    key_value["b"] = 56
    key_value["abcde"] = 2
    key_value["abbb"] = 34
    key_value["arnd"] = 15
    key_value["d"] = 12
    key_value["c"] = 24
    key_value["f"] = 18
    key_value["e"] = 323

    print("\n example1 - sort by KEY, ASC");
    print(sorted(key_value.items(), key=lambda kv: (kv[0], kv[1])))  # key, value
    print(sorted(key_value.items(), key=lambda kv: (kv[0])))  # key, value

    print("\n example2 - sort by KEY DESC");
    print(sorted(key_value.items(), key=lambda kv: (kv[0]), reverse=True))  # key, value

    print("\n example3 - printing on each line and sort by KEY");
    for i, value in sorted(key_value.items()):
        print((i, value), end="\n")

    print("\n example3 - sort by VALUE, ASC");
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))  # value, key

    print("\n printed sorted keys only");
    print(sorted(key_value.keys()))

    print("\n printed sorted values only");
    print(sorted(key_value.values()))


sort_dict_by_key_value()
