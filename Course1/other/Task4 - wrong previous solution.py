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
    possible_telemarketers_set.clear()

    for item in calls_list:
        calling_tel_number = item[0]
        calling_tel_type = get_type_of_number(calling_tel_number)

        if calling_tel_type == TelTypes.not_valid.value:
            print("calling_tel_type is not in valid format!")
        # add the number as possible telemarketer
        if calling_tel_type == TelTypes.telemarketer.value:
            possible_telemarketers_set.add(calling_tel_number)
        # check the answering tel_number
        verify_tel_number(item[1])


def check_texts_data(texts_list):
    if len(possible_telemarketers_set) == 0:
        raise Exception("->check_texts_data: you need to call check_texts_data() "
                        "after check_calls_data() to fill in the possible_telemarketers_set")
    for item in texts_list:
        verify_tel_number(item[0])  # checking the sending texts tel_number
        verify_tel_number(item[1])  # checking the receiving texts tel_number


'''
Takes the telephone number and if it has telemarketer format and exists in possible_telemarketers_set 
than deletes it otherwise does nothing
ARGS:
    tel_number (string)
'''


def verify_tel_number(tel_number):
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


def print_sorted_telemarketers_new_line():
    print("length of possible_telemarketers_set = {}".format(len(possible_telemarketers_set)))
    print("These numbers could be telemarketers: ")
    print(*sorted(possible_telemarketers_set), sep='\n')  # in lexicographic order with no duplicates


def main():
    create_telemarketers_set()
    print_sorted_telemarketers_new_line()


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
    print("---------------------------------------------")
    print("->test_check_calls_data:start")
    test_calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                       ["1401111111", "(034)78655", "1/9/2016  7:31", "15"],  # 1401111111 -tele
                       ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],
                       ["1409999999", "90365 06212", "1/9/2016  7:31", "15"],
                       ["1408888888", "90365 06212", "1/9/2016  7:31", "15"],  # 1408888888 - telemarketer
                       ["90365 06212", "1409999999", "1/9/2016  7:31", "15"],  # 1409999999 - not telemarketer
                       ["1402222222", "83019 53227", "1/9/2016  7:31", "15"],  # 1402222222 - tele
                       ["1403333333", "1404444444", "1/9/2016  7:31", "15"],  # 1403333333 - tele, 1404444444 - not
                       ["(04456)69245029", "1405555555", "1/9/2016  7:31", "15"]]  # 1405555555 - not telemarketer
    check_calls_data(test_calls_list)
    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    assert len(possible_telemarketers_set) == 4
    assert ("1401111111" in possible_telemarketers_set)
    assert ("1408888888" in possible_telemarketers_set)
    assert ("1402222222" in possible_telemarketers_set)
    assert ("1403333333" in possible_telemarketers_set)
    assert ("1404444444" not in possible_telemarketers_set)
    print("->test_check_calls_data: is finished")


def test_check_check_texts_data():
    print("---------------------------------------------")
    print("->test_check_check_texts_data:start")
    test_texts_list = [["1401111111", "90365 06212", "1/9/2016  6:03:22 AM"],  # 1401111111 - not telemarketer
                       ["(04456)69245029", "1403333333", "1/9/2016  7:31"],  # 1403333333 - not telemarketer
                       ["78130 00821", "(034)78655", "1/9/2016  7:31"]]
    check_texts_data(test_texts_list)
    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    assert len(possible_telemarketers_set) == 2
    assert ("1401111111" not in possible_telemarketers_set)  # should be deleted
    assert ("1408888888" in possible_telemarketers_set)
    assert ("1402222222" in possible_telemarketers_set)
    assert ("1403333333" not in possible_telemarketers_set)  # should be deleted
    assert ("1404444444" not in possible_telemarketers_set)
    print("->test_check_check_texts_data: is finished")


def test_verify_tel_number():
    print("---------------------------------------------")
    print("->test_verify_tel_number:start")
    test_calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                       ["1401111111", "(034)78655", "1/9/2016  7:31", "15"],  # 1401111111 -tele
                       ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],
                       ["1409999999", "90365 06212", "1/9/2016  7:31", "15"],
                       ["1408888888", "90365 06212", "1/9/2016  7:31", "15"],  # 1408888888 - telemarketer
                       ["90365 06212", "1409999999", "1/9/2016  7:31", "15"],  # 1409999999 - not telemarketer
                       ["1402222222", "83019 53227", "1/9/2016  7:31", "15"],  # 1402222222 - tele
                       ["1403333333", "1404444444", "1/9/2016  7:31", "15"],  # 1403333333 - tele, 1404444444 - not
                       ["(04456)69245029", "1405555555", "1/9/2016  7:31", "15"]]  # 1405555555 - not telemarketer
    check_calls_data(test_calls_list)
    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    # case1 - 1408888888 has telemarketer type and exists in possible_telemarketers_set
    verify_tel_number("1408888888")
    assert ("1408888888" not in possible_telemarketers_set)  # must be deleted
    assert len(possible_telemarketers_set) == 3
    print("case1: possible_telemarketers_set=" + str(possible_telemarketers_set))
    # case2 - 140777777 has telemarketer type but does not exist in possible_telemarketers_set
    verify_tel_number("140777777")  # must not change possible_telemarketers_set
    assert len(possible_telemarketers_set) == 3
    # case3 - not a telemarketer format and does not exist in possible_telemarketers_set
    verify_tel_number("84577 7777")  # must not change possible_telemarketers_set
    assert len(possible_telemarketers_set) == 3
    print("->test_check_check_texts_data: is finished")


def test():
    print("START ALL TESTS....")
    test_get_type_of_number()
    test_check_calls_data()
    test_check_check_texts_data()
    test_verify_tel_number()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

# test()
main()