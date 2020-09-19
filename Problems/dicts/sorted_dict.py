def sort_dict_by_key_value():
    key_value = {}
    key_value["b"] = 56
    key_value["bcfgfg"] = 34
    key_value["abcde"] = 2
    key_value["abbb"] = 34
    key_value["abbbnob"] = 34
    key_value["al"] = 34
    key_value["arnd"] = 15
    key_value["d"] = 12
    key_value["c"] = 34
    key_value["f"] = 18
    key_value["e"] = 323

    print("\n printed sorted keys only");
    print(sorted(key_value.keys()))

    print("\n printed sorted values only");
    print(sorted(key_value.values()))

    print("\n printed sorted KEYS only, DESC");
    print(sorted(key_value, key=lambda k: (-key_value[k], k)))

    print("\n printed sorted KEYS only, ASC");
    print(sorted(key_value, key=lambda k: (key_value[k], k)))

    print("\n EXAMPLE 1 - sort by KEY ONLY, ASC");
    print(sorted(key_value.items(), key=lambda kv: (kv[0], kv[1])))
    print(sorted(key_value.items(), key=lambda kv: (kv[0])))

    print("\n EXAMPLE 2 - sort by KEY ONLY, DESC");
    print(sorted(key_value.items(), key=lambda kv: (kv[0]), reverse=True))

    print("\n EXAMPLE 3 - sort by VALUE ONLY, DESC");
    print(sorted(key_value.items(), key=lambda kv: (kv[1]), reverse=True))

    print("\n EXAMPLE 4 - printing on each line and sort by KEY");
    for i, value in sorted(key_value.items()):
        print((i, value), end="\n")

    print("\n EXAMPLE 5 - sort by VALUE, ASC and KEY, ASC");
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

    print("\n EXAMPLE 6 - sort by VALUE, ASC and KEY, DESC");
    print(sorted(key_value.items(), key=lambda kv: (-kv[1], kv[0]), reverse=True))

    print("\n EXAMPLE 7 - sort by VALUE, DESC and KEY, DESC");
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

    print("\n EXAMPLE 8 - sort by VALUE, DESC and KEY, ASC");
    print(sorted(key_value.items(), key=lambda kv: (-kv[1], kv[0])))


sort_dict_by_key_value()
