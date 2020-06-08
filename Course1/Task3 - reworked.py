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


bangalore_codes_set = set()
amount_fixed_line_bangalor_responses = 0
amount_all_fixed_line_bangalor_calls = 0


def create_bangalore_numbers_set(calls_list):
    bangalore_codes_set.clear()
    global amount_fixed_line_bangalor_responses
    amount_fixed_line_bangalor_responses = 0
    global amount_all_fixed_line_bangalor_calls
    amount_all_fixed_line_bangalor_calls = 0

    for item in calls_list:
        calling_tel_number = item[0]
        is_fixed_line_bangalor_caller, code_area = is_bangalore_area(calling_tel_number)
        # print("is_fixed_line_bangalor_caller={}, code_area={}".format(is_fixed_line_bangalor_caller, code_area))

        # if we are calling from bangalor fixed line number
        if is_fixed_line_bangalor_caller:
            answering_tel_num = item[1]
            # check the type of receiver number
            is_bangalore_receiver, code_area = is_bangalore_area(answering_tel_num)
            if code_area != TelTypes.not_valid.value:
                bangalore_codes_set.add(code_area)

            # counting amount for partB
            if is_bangalore_receiver:
                amount_fixed_line_bangalor_responses += 1
            amount_all_fixed_line_bangalor_calls += 1


def get_fixed_line_area_code(tel_number):
    index = tel_number.find(")")
    if index != -1:
        return tel_number[1: index]
    else:
        print("Could not find ')' in the telephone number!")
        # raise Exception("There is no ')' in the provided tel number! ")


def is_bangalore_area(tel_number):
    type, code = get_type_of_number(tel_number)
    return type == TelTypes.fixed_line.value, code


def get_type_of_number(tel_number):
    if tel_number == "":
        raise Exception('tel_number should not be an empty string!')
    # print("->get_type_of_number: tel_number={}".format(tel_number))
    if tel_number[0] == "(" and tel_number[1] == "0":
        return TelTypes.fixed_line.value, get_fixed_line_area_code(tel_number)
    if tel_number[0:3] == "140" and " " not in tel_number:
        return TelTypes.telemarketer.value, tel_number[0: 3]
    # mobile code - first four digits, and they always start with 7, 8 or 9.
    if len(tel_number.split(" ")) == 2 and (int(tel_number[0]) in range(7, 10)):
        return TelTypes.mobile.value, tel_number[0: 4]

    print("tel_number is not in valid format!")
    # raise Exception('tel_number is not in valid format!')
    return TelTypes.not_valid.value, TelTypes.not_valid.value


def calculate_percentage():
    if amount_all_fixed_line_bangalor_calls == 0:
        return 0
    if (amount_all_fixed_line_bangalor_calls < amount_fixed_line_bangalor_responses):
        raise Exception(
            'amount_all_fixed_line_bangalor_calls must be equal or larger than amount_fixed_line_bangalor_responses!')

    return (amount_fixed_line_bangalor_responses * 100) / amount_all_fixed_line_bangalor_calls


def get_sorted_bangalore_codes_set():
    return sorted(bangalore_codes_set)


def print_answer_part_a():
    print("The numbers called by people in Bangalore have codes:")
    print(*get_sorted_bangalore_codes_set(), sep="\n")


def print_answer_part_b():
    percentage = int(calculate_percentage())  # only 2 digits
    print("{} percent of calls from fixed lines in Bangalore are "
          "calls to other fixed lines in Bangalore.".format(percentage))


def main():
    create_bangalore_numbers_set(calls)
    print_answer_part_a()
    print_answer_part_b()


# TEST CASES----------------------------------------------
def test_get_type_of_number():
    print("---------------------------------------------")
    print("->test_get_type_of_number:start")
    # mobile
    tel_type, code = get_type_of_number("93427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "9342")
    tel_type, code = get_type_of_number("83427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "8342")
    tel_type, code = get_type_of_number("73427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "7342")
    tel_type, code = get_type_of_number("23427 40118")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == TelTypes.not_valid.value, "expected=0, actual={}".format(code)
    # fixed_line
    tel_type, code = get_type_of_number("(04344)228249")
    assert (tel_type == TelTypes.fixed_line.value)
    assert code == "04344", "expected=04344, actual={}".format(code)
    tel_type, code = get_type_of_number("(140)8371942")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == TelTypes.not_valid.value, "expected=0, actual={}".format(code)
    # telemarketer
    tel_type, code = get_type_of_number("1408371942")
    assert (tel_type == TelTypes.telemarketer.value)
    assert (code == "140")
    tel_type, code = get_type_of_number("14083 71942")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == TelTypes.not_valid.value, "expected=0, actual={}".format(code)
    print("->test_get_type_of_number: is finished")


def test_get_fixed_line_area_code():
    print("---------------------------------------------")
    print("->get_fixed_line_area_code:start")
    assert (get_fixed_line_area_code("(04344)228249") == "04344")
    assert (get_fixed_line_area_code("(080)228249") == "080")
    assert (get_fixed_line_area_code("(080228249") != "080")
    print("->get_fixed_line_area_code: is finished")


def test_create_bangalore_numbers_set_1():
    print("---------------------------------------------")
    print("->test_create_bangalore_numbers_set_1:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(083)69245029", "1408371942", "1/9/2016  7:31", "15"]]
    create_bangalore_numbers_set(calls_list)
    print("bangalore_codes_set=" + str(bangalore_codes_set))
    assert (len(bangalore_codes_set) == 4)

    expected_result = 1
    assert amount_fixed_line_bangalor_responses == expected_result, \
        "Actual result= {}, expected result = {}".format(amount_fixed_line_bangalor_responses, expected_result)

    expected_result = 5
    assert amount_all_fixed_line_bangalor_calls == expected_result, \
        "Actual result= {}, expected result = {}".format(amount_all_fixed_line_bangalor_calls, expected_result)

    assert (('034' in bangalore_codes_set) == True)
    assert (('8301' in bangalore_codes_set) == True)
    assert (('9036' in bangalore_codes_set) == True)
    assert (('140' in bangalore_codes_set) == True)
    print("->test_create_bangalore_numbers_set_1: is finished")


def test_create_bangalore_numbers_set_2():
    print("---------------------------------------------")
    print("->test_create_bangalore_numbers_set_2:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)2222222", "(034)78655", "1/9/2016  7:31", "15"],
                  ["11111111111", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "(003)65 06212", "1/9/2016  7:31", "15"],
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"]]
    create_bangalore_numbers_set(calls_list)
    print("bangalore_codes_set=" + str(bangalore_codes_set))
    assert (len(bangalore_codes_set) == 4)

    expected_result = 4
    assert amount_fixed_line_bangalor_responses == expected_result, \
        "Actual result= {}, expected result = {}".format(amount_fixed_line_bangalor_responses, expected_result)

    expected_result = 5
    assert amount_all_fixed_line_bangalor_calls == expected_result, \
        "Actual result= {}, expected result = {}".format(amount_all_fixed_line_bangalor_calls, expected_result)

    assert (('080' in bangalore_codes_set) == True)
    assert (('003' in bangalore_codes_set) == True)
    assert (('8301' in bangalore_codes_set) == True)
    assert (('034' in bangalore_codes_set) == True)

    print("->test_create_bangalore_numbers_set_2: is finished")


def test_calculate_percentage_1():
    print("---------------------------------------------")
    print("->test_calculate_percentage_1:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)2222222", "(034)78655", "1/9/2016  7:31", "15"],
                  ["11111111111", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "(003)65 06212", "1/9/2016  7:31", "15"],
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"], # not fixed line answer
                  ["(082)666666", "1401953227", "1/9/2016  7:31", "15"]]    # not fixed line answer
    create_bangalore_numbers_set(calls_list)
    print("bangalore_codes_set= " + str(bangalore_codes_set))
    # 6 calls, 4 answers with fixed line
    actual_result = calculate_percentage()
    expected_result = (4 * 100) / 6  # 4 - answers, 6 - all calls from bangalor

    assert actual_result == expected_result, \
        "Actual result= {}, expected result = {}".format(actual_result, expected_result)

    print("->test_calculate_percentage_1: is finished")


def test_calculate_percentage_2():
    print("---------------------------------------------")
    print("->test_calculate_percentage_2:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)2222222", "(034)78655", "1/9/2016  7:31", "15"],
                  ["11111111111", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "66666 6666", "1/9/2016  7:31", "15"],
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"]]
    create_bangalore_numbers_set(calls_list)
    print("bangalore_codes_set= " + str(bangalore_codes_set))
    # 5 calls, 3 answers fixed line
    actual_result = calculate_percentage()
    expected_result = (3 * 100) / 5  # 3 - answers, 5 - all calls from bangalor

    assert actual_result == expected_result, \
        "Actual result= {}, expected result = {}".format(actual_result, expected_result)

    print("->test_calculate_percentage_2: is finished")


def test_get_sorted_bangalore_codes_set():
    print("---------------------------------------------")
    print("->test_get_sorted_bangalore_codes_set:start")
    calls_list = [["(084)44444444", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(0843)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(0310)2222222", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(0334670)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(09910)44444444", "66666 6666", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "(084)44444444", "1/9/2016  7:31", "15"],
                  ["(081)55555555", "14044444444", "1/9/2016  7:31", "15"],
                  ["(081)55555555", "(0334670)44444444", "1/9/2016  7:31", "15"],
                  ["(081)55555555", "774554 4788", "1/9/2016  7:31", "15"],
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(020)666666", "75674 53227", "1/9/2016  7:31", "15"]]
    create_bangalore_numbers_set(calls_list)
    print("bangalore_codes_set= " + str(bangalore_codes_set))
    sorted_result = list(get_sorted_bangalore_codes_set())
    expected_result = ["0334670", "034", "080", "084", "140", "7567", "7745", "8301", "9036"]
    assert sorted_result == expected_result, \
        "expected={}, \n actual={}".format(expected_result, sorted_result)
    print("->test_get_sorted_bangalore_codes_set: is finished")


def test():
    print("START ALL TESTS....")
    test_get_type_of_number()
    test_get_fixed_line_area_code()
    test_create_bangalore_numbers_set_1()
    test_create_bangalore_numbers_set_2()
    test_calculate_percentage_1()
    test_calculate_percentage_2()
    test_get_sorted_bangalore_codes_set()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

#test()
main()
