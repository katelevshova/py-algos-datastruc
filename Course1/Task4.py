"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import Enum

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


class TelTypes(Enum):
    not_valid = 0
    fixed_line = 1
    mobile = 2
    telemarketer = 3


possible_telemarketers_set = set()


def check_calls_data(calls_list):
    for item in calls_list:
        calling_tel_number = item[0]
        calling_tel_type = get_type_of_number(calling_tel_number)

        if calling_tel_type == TelTypes.not_valid.value:
            print("calling_tel_type is not in valid format!")
        # add the number as possible telemarketer
        if calling_tel_type == TelTypes.telemarketer.value:
            possible_telemarketers_set.add(calling_tel_number)
        # check the answering tel_number
        verify_number(item[1])


def check_texts_data(texts_list):
    if len(possible_telemarketers_set) == 0:
        raise Exception("->check_texts_data: you need to call check_texts_data() "
                        "after check_calls_data() to fill in the possible_telemarketers_set")
    for item in texts_list:
        verify_number(item[0])  # checking the sending texts tel_number
        verify_number(item[1])  # checking the receiving texts tel_number


def verify_number(tel_number):
    # telemarketers never send and receive texts so if the number is found and it exists
    # in the possible_telemarketers_set we need to delete it because it is not considered a telemarketer
    tel_type = get_type_of_number(tel_number)

    if tel_type == TelTypes.not_valid.value:
        print("tel_number {} is not in valid format!".format(tel_number))

    if tel_type == TelTypes.telemarketer.value:
        possible_telemarketers_set.discard(tel_number)


def get_type_of_number(tel_number):
    if (tel_number == ""):
        raise Exception('tel_number should not be an empty string!')
    # print("->get_type_of_number: tel_number={}".format(tel_number))
    if tel_number[0] == "(" and tel_number[1] == "0":
        return TelTypes.fixed_line.value
    if tel_number[0:3] == "140" and " " not in tel_number:
        return TelTypes.telemarketer.value
    if len(tel_number.split(" ")) == 2 and (int(tel_number[0]) in range(7, 10)):
        return TelTypes.mobile.value

    return TelTypes.not_valid.value


def create_telemarketers_set():
    check_calls_data(calls)
    check_texts_data(texts)


def print_all_telemarketers_new_line():
    print("These numbers could be telemarketers: ")
    print(*possible_telemarketers_set, sep='\n')


def main():
    create_telemarketers_set()
    print_all_telemarketers_new_line()


# TEST CASES----------------------------------------------
def test_get_type_of_number():
    print("---------------------------------------------")
    print("->test_get_type_of_number:start")
    # mobile
    assert (get_type_of_number("93427 40118") == TelTypes.mobile.value)
    assert (get_type_of_number("83427 40118") == TelTypes.mobile.value)
    assert (get_type_of_number("73427 40118") == TelTypes.mobile.value)
    assert (get_type_of_number("23427 40118") == TelTypes.not_valid.value)
    # fixed_line
    assert (get_type_of_number("(04344)228249") == TelTypes.fixed_line.value)
    assert (get_type_of_number("(140)8371942") == TelTypes.not_valid.value)
    # telemarketer
    assert (get_type_of_number("1408371942") == TelTypes.telemarketer.value)
    assert (get_type_of_number("14083 71942") == TelTypes.not_valid.value)
    print("->test_get_type_of_number: is finished")


def test_check_calls_data():
    test_calls_list = list()


def test():
    print("START ALL TESTS....")
    test_get_type_of_number()
    test_check_calls_data()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

test()
# main()
