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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


class TelTypes(Enum):
    not_valid = 0
    fixed_line = 1
    mobile = 2
    telemarketer = 3


bangalore_numbers_dict = dict()
# dictionary property:
to_bangalore_id = 'to_bangalore'


def create_bangalore_numbers_dict(calls_list):
    for item in calls_list:
        calling_tel_number = item[0]
        calling_tel_type = get_type_of_number(calling_tel_number)

        if calling_tel_type == TelTypes.not_valid.value:
            print("tel_number is not in valid format!")
            # raise Exception('tel_number is not in valid format!')

        if calling_tel_type == TelTypes.fixed_line.value:
            answering_tel_num = item[1]
            to_bangalore = is_bangalore_area(answering_tel_num)
            info_dict = {to_bangalore_id: to_bangalore}

            if calling_tel_number not in bangalore_numbers_dict:
                bangalore_numbers_dict[calling_tel_number] = list()

            bangalore_numbers_dict[calling_tel_number].append(info_dict)


def get_area_code(tel_numer):
    index = tel_numer.find(")")
    if index != -1:
        return tel_numer[1: index]
    else:
        print("Could not find ')' in the telephone number!")
        # raise Exception("There is no ')' in the provided tel number! ")


def is_bangalore_area(tel_number):
    return (get_type_of_number(tel_number) == TelTypes.fixed_line.value)


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


def get_unique_area_codes(dictionary):
    result_set = set()
    for tel_number in dictionary.keys():  # keys are always unique
        # print("get_unique_area_codes="+str(tel_number))
        result_set.add(get_area_code(tel_number))
    return result_set

def get_amount_calling_from_bangalor(dictionary):
    return len(dictionary.keys())

def get_amount_answering_in_bangalor(dictionary):

    return 0

def print_answer_part_a():
    print("The numbers called by people in Bangalore have codes:")
    print(*get_unique_area_codes(bangalore_numbers_dict), sep="\n")


def print_answer_part_b():
    percentage = ""  # only 2 digits
    print("{} percent of calls from fixed lines in Bangalore are "
          "calls to other fixed lines in Bangalore.".format(percentage))


def main():
    create_bangalore_numbers_dict(calls)
    print_answer_part_a()
    print_answer_part_b()


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


def test_get_area_code():
    print("---------------------------------------------")
    print("->test_get_area_code:start")
    assert (get_area_code("(04344)228249") == "04344")
    assert (get_area_code("(080)228249") == "080")
    assert (get_area_code("(080228249") != "080")
    print("->test_get_area_code: is finished")


def test_create_bangalore_numbers_dict():
    print("---------------------------------------------")
    print("->test_create_bangalore_numbers_dict:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"]]
    create_bangalore_numbers_dict(calls_list)
    print("bangalore_numbers_dict=" + str(bangalore_numbers_dict))
    assert (len(bangalore_numbers_dict.keys()) == 2)
    assert (bangalore_numbers_dict["(080)69245029"][0][to_bangalore_id] == True)
    assert (bangalore_numbers_dict["(04456)69245029"][1][to_bangalore_id] == False)
    print("->test_create_bangalore_numbers_dict: is finished")


def test_get_unique_area_codes():
    print("---------------------------------------------")
    print("->test_get_unique_area_codes:start")
    test_dict = {
        '(080)3333333': [{'to_bangalore': True},
                         {'to_bangalore': False}],
        '(080)2222222': [{'to_bangalore': True},
                         {'to_bangalore': False}],
        '(04456)69245029': [{'to_bangalore': False},
                            {'to_bangalore': False}]}
    result_set = get_unique_area_codes(test_dict)
    # print(result_set)
    assert (('080' in result_set) == True)
    assert (('04456' in result_set) == True)
    assert (len(result_set) == 2)
    print("->test_get_unique_area_codes: is finished")

def test_get_amount_answering_in_bangalor():
    print("---------------------------------------------")
    print("->test_get_amount_answering_in_bangalor:start")
    test_dict = {
        '(080)3333333': [{'to_bangalore': True},
                         {'to_bangalore': False},
                         {'to_bangalore': False},
                         {'to_bangalore': False},
                         {'to_bangalore': True}],
        '(080)2222222': [{'to_bangalore': True},
                         {'to_bangalore': False}],
        '(04456)69245029': [{'to_bangalore': False},
                            {'to_bangalore': False}]}

def test():
    print("START ALL TESTS....")
    test_get_type_of_number()
    test_get_area_code()
    test_create_bangalore_numbers_dict()
    test_get_unique_area_codes()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

test()
main()
