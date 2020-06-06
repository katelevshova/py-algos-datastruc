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

def add_telemarketers_from_calls(calls_list):
    for item in calls_list:
        calling_tel_number = item[0]
        answering_tel_number = item[1]
        print("calling_tel_number={}, answering_tel_number={}".format(calling_tel_number, answering_tel_number))

        calling_tel_type = get_type_of_number(calling_tel_number)
        if calling_tel_type == TelTypes.not_valid.value:
            print("calling_tel_type is not in valid format!")

        answering_tel_type = get_type_of_number(answering_tel_number)
        if answering_tel_type == TelTypes.not_valid.value:
            print("answering_tel_type is not in valid format!")

        if calling_tel_type == TelTypes.telemarketer.value:
            possible_telemarketers_set.add(calling_tel_number)

        if answering_tel_type == TelTypes.telemarketer.value:
            # telemarketers never receive incoming calls so we don't need to add to possible_telemarketers_set
            # but if this number exists in the possible_telemarketers_set we need to delete it
            # discard() removes only if the item exists
            possible_telemarketers_set.discard(answering_tel_number)


def add_telemarketers_from_texts(texts_list):
    for item in texts_list:
        sending_tel_number = item[0]
        receiving_tel_number = item[1]
        print("sending_tel_number={}, receiving_tel_number={}".format(sending_tel_number, receiving_tel_number))

        sending_tel_type = get_type_of_number(sending_tel_number)
        





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
    add_telemarketers_from_calls(calls)
    add_telemarketers_from_texts(texts)

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

def test_create_telemarketers_set():
    test_calls_list = list()


def test():
    print("START ALL TESTS....")
    test_get_type_of_number()
    test_create_telemarketers_set()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

test()
#main()