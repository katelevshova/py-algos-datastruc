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
verification_set = set()

'''
Checks all items in calls list. For each item checks the type of the number called. If the called
number does not exists in the verification_set we add it to the possible_telemarketers_set.
We verify the answered number and add it to verification_set.  If answered number exists 
in possible_telemarketers_set we discard it because the telemarketer number cannot answer the calls.  
'''


def check_calls_data(calls_list):
    possible_telemarketers_set.clear()
    verification_set.clear()

    for item in calls_list:
        # add the caller tel number as possible telemarketer
        if item[0] not in verification_set:
            possible_telemarketers_set.add(item[0])
        # check the answering tel_number
        verify_tel_number(item[1])


'''
Checks all items in texts list. For each item checks the type of the number sent message and received. 
If it is a telemarketer format, we remove the number from possible_telemarketers_set because telemarketers only call
but never send or receive text messages.
ARGS:
     texts_list (list) - list of lists.  Example:
                    [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM"],
                    ["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM"]]
'''


def check_texts_data(texts_list):
    if len(possible_telemarketers_set) == 0:
        raise Exception("->check_texts_data: you need to call check_texts_data() "
                        "after check_calls_data() to fill in the possible_telemarketers_set")
    for item in texts_list:
        verify_tel_number(item[0])  # checking the sending texts tel_number
        verify_tel_number(item[1])  # checking the receiving texts tel_number


'''
Takes the telephone number and if it has telemarketer format adds it into verification_set
and if it exists in possible_telemarketers_set deletes it. Otherwise does nothing
ARGS:
    tel_number (string)
'''


def verify_tel_number(tel_number):
    # telemarketers never send and receive texts so if the number is found and it exists
    # in the possible_telemarketers_set we need to delete it because it is not considered a telemarketer
    verification_set.add(tel_number)
    possible_telemarketers_set.discard(tel_number)


'''
Returns type of the telephone number
ARGS:
    tel_number (string)
RETURN:
    telephone type (int) from TelTypes enumeration: not_valid = 0, fixed_line = 1, mobile = 2, telemarketer = 3
Example:    if "93427 40118", returned tel_type = 2
            if "1408371942", returned tel_type = 3
            if "(0834)343434", returned tel_type = 1
            if "0834)343434", returned tel_type = 0
            if "9342740118", returned tel_type = 0    
'''


def get_type_of_number(tel_number):
    if tel_number == "":
        raise Exception('tel_number should not be an empty string!')
    # print("->get_type_of_number: tel_number={}".format(tel_number))
    if tel_number[0] == "(" and tel_number[1] == "0":
        return TelTypes.fixed_line.value
    if tel_number[0:3] == "140" and " " not in tel_number:
        return TelTypes.telemarketer.value
    if len(tel_number.split(" ")) == 2 and (int(tel_number[0]) in range(7, 10)):
        return TelTypes.mobile.value
    print("tel_number {} is not in valid format!".format(tel_number))
    return TelTypes.not_valid.value


'''
Creates possible_telemarketers_set based on the data from 2 files - calls.csv and texts.csv
'''


def create_telemarketers_set():
    check_calls_data(calls)
    check_texts_data(texts)


def print_sorted_telemarketers_new_line():
    # print("length of possible_telemarketers_set = {}".format(len(possible_telemarketers_set)))
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

    test_calls_list = [["7777 77777", "99999 99999", "1/9/2016  6:46:56 AM", "165"],
                       ["44444 4444", "55555 55555", "1/9/2016  6:46:56 AM", "165"],
                       ["66666 6666", "7777 77777", "1/9/2016  6:46:56 AM", "165"],
                       ["1403333333", "(080)111111", "1/9/2016  7:31", "15"]]
    check_calls_data(test_calls_list)

    print("verification_set=" + str(verification_set))
    assert len(verification_set) == 4
    assert ("99999 99999" in verification_set)
    assert ("55555 55555" in verification_set)
    assert ("7777 77777" in verification_set)
    assert ("(080)111111" in verification_set)

    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    assert len(possible_telemarketers_set) == 3
    assert ("44444 4444" in possible_telemarketers_set)
    assert ("66666 6666" in possible_telemarketers_set)
    assert ("1403333333" in possible_telemarketers_set)
    assert ("7777 77777" not in possible_telemarketers_set)

    print("->test_check_calls_data: is finished")


def test_check_check_texts_data():
    print("---------------------------------------------")
    print("->test_check_check_texts_data:start")
    test_texts_list = [["1401111111", "90365 06212", "1/9/2016  6:03:22 AM"],
                       ["(04456)69245029", "(080)787878", "1/9/2016  7:31"],
                       ["44444 4444", "0000 00000", "1/9/2016  6:46:56 AM", "165"],
                       ["78130 00821", "66666 6666", "1/9/2016  7:31"]]
    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    check_texts_data(test_texts_list)
    print("verification_set=" + str(verification_set))
    assert len(verification_set) == 12  # we add sending and receiving msg to verification list
    assert ("1401111111" in verification_set)
    assert ("0000 00000" in verification_set)
    assert ("44444 4444" in verification_set)

    # 44444 4444 and 66666 6666 not must be removed from possible_telemarketers_set
    print("after removing numbers from TEXTS file, possible_telemarketers_set=" + str(possible_telemarketers_set))
    assert len(possible_telemarketers_set) == 1
    assert ("44444 4444" not in possible_telemarketers_set)  # should be deleted
    assert ("66666 6666" not in possible_telemarketers_set)  # should be deleted
    assert ("1403333333" in possible_telemarketers_set)
    print("->test_check_check_texts_data: is finished")


def test_verify_tel_number():
    print("---------------------------------------------")
    print("->test_verify_tel_number:start")
    test_calls_list = [["7777 77777", "99999 99999", "1/9/2016  6:46:56 AM", "165"],
                       ["44444 4444", "55555 55555", "1/9/2016  6:46:56 AM", "165"],
                       ["66666 6666", "7777 77777", "1/9/2016  6:46:56 AM", "165"],
                       ["1403333333", "(080)111111", "1/9/2016  7:31", "15"]]
    check_calls_data(test_calls_list)
    print("possible_telemarketers_set=" + str(possible_telemarketers_set))
    # case1 - check any not existed number
    verify_tel_number("1408888888")
    assert ("1408888888" not in possible_telemarketers_set)  # must be deleted
    assert ("1408888888" in verification_set)  # must be added for verification
    assert len(possible_telemarketers_set) == 3
    print("case1: possible_telemarketers_set=" + str(possible_telemarketers_set))
    # case2 - check existed number among callers
    verify_tel_number("66666 6666")
    assert ("66666 6666" in verification_set)
    assert ("66666 6666" not in possible_telemarketers_set)
    assert len(possible_telemarketers_set) == 2
    print("case2: possible_telemarketers_set=" + str(possible_telemarketers_set))
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
