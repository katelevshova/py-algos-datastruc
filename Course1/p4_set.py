"""
Read file into texts and calls.
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


class Amount:
    bangalor_responses = 0
    all_bangalor_calls = 0


codes_dialed_by_bangalor_set = set()

'''
Checks all items in calls list. For each item checks if the caller is from Bangalore by checking its area code and type.
If the caller is from Bangalor it saves the area code of the number answered the call into a
codes_dialed_by_bangalor_set. At the same time counts the total amount of calls from Bangalor and the amount of 
responses in Bangalor from numbers in Bangalor. 
'''


def create_codes_dialed_by_bangalor_set(calls_list):
    codes_dialed_by_bangalor_set.clear()
    Amount.bangalor_responses = 0
    Amount.all_bangalor_calls = 0

    for item in calls_list:
        calling_tel_number = item[0]
        tel_type_caller, code_area_caller = get_teltype_and_codearea_of_number(calling_tel_number)

        # if we are calling from bangalor fixed line number
        if is_bangalore_area(code_area_caller):
            answering_tel_num = item[1]
            # check the type of receiver number
            tel_type_receiver, code_area_receiver = get_teltype_and_codearea_of_number(answering_tel_num)

            # counting amount for partB
            Amount.all_bangalor_calls += 1
            if is_bangalore_area(code_area_receiver):
                Amount.bangalor_responses += 1
            # adding unique code area of receiver for part A
            if code_area_receiver != str(TelTypes.not_valid.value):
                codes_dialed_by_bangalor_set.add(code_area_receiver)

            # print("tel_type_caller={}, code_area_caller={} | "
            #     "tel_type_receiver={}, code_area_receiver={}".format(tel_type_caller, code_area_caller,
            #                                                         tel_type_receiver, code_area_receiver))


def get_fixed_line_area_code(tel_number):
    index = tel_number.find(")")
    if index != -1:
        return tel_number[1: index]
    else:
        print("Could not find ')' in the telephone number!")
        # raise Exception("There is no ')' in the provided tel number! ")


def is_bangalore_area(area_code):
    return area_code == "080"


'''
Returns type of the telephone number and it's area code
ARGS:
    tel_number (string)
RETURN:
    telephone type (int) from TelTypes enumeration: not_valid = 0, fixed_line = 1, mobile = 2, telemarketer = 3
    area code (string) 
Example:    if "93427 40118", returned tel_type = 2, area_code="9342"
            if "1408371942", returned tel_type = 3, area_code="140"
            if "(0834)343434", returned tel_type = 1, area_code="0834" 
            if "0834)343434", returned tel_type = 0, area_code="0"
            if "9342740118", returned tel_type = 0, area_code="0"    
'''


def get_teltype_and_codearea_of_number(tel_number):
    if tel_number == "":
        raise Exception('tel_number should not be an empty string!')
    # print("->get_teltype_and_codearea_of_number: tel_number={}".format(tel_number))
    if tel_number[0] == "(" and tel_number[1] == "0":
        return TelTypes.fixed_line.value, get_fixed_line_area_code(tel_number)
    if tel_number[0:3] == "140" and " " not in tel_number:
        return TelTypes.telemarketer.value, tel_number[0: 3]
    # mobile code - first four digits, and they always start with 7, 8 or 9.
    if len(tel_number.split(" ")) == 2 and (int(tel_number[0]) in range(7, 10)):
        return TelTypes.mobile.value, tel_number[0: 4]

    print("tel_number {} is not in valid format!".format(tel_number))
    # raise Exception('tel_number is not in valid format!')
    return TelTypes.not_valid.value, str(TelTypes.not_valid.value)


def calculate_percentage():
    if Amount.all_bangalor_calls == 0:
        return 0
    if Amount.all_bangalor_calls < Amount.bangalor_responses:
        raise Exception('all_bangalor_calls must be equal or larger than bangalor_responses!')
    percentage = (Amount.bangalor_responses * 100) / Amount.all_bangalor_calls
    # print("->calculate_percentage: percentage={}".format(percentage))
    return percentage


def get_2decimal_digits(number):
    # str(round(number, 2)) returns 25.0 if number ==25, we need 25.00
    formatted_result = '{:0.2f}'.format(number)
    # print("->get_2decimal_digits: number={}, formatted_result={} ".format(number, formatted_result))
    return formatted_result


def get_sorted_codes_dialed_by_bangalor_set():
    return sorted(codes_dialed_by_bangalor_set)


def print_answer_part_a():
    print("The numbers called by people in Bangalore have codes:")
    print(*get_sorted_codes_dialed_by_bangalor_set(), sep="\n")


def print_answer_part_b():
    percentage = get_2decimal_digits(calculate_percentage())
    print("{} percent of calls from fixed lines in Bangalore are "
          "calls to other fixed lines in Bangalore.".format(percentage))


def main():
    create_codes_dialed_by_bangalor_set(calls)
    print_answer_part_a()
    print_answer_part_b()


# TEST CASES----------------------------------------------
def test_get_teltype_and_codearea_of_number():
    print("---------------------------------------------")
    print("->test_get_teltype_and_codearea_of_number:start")
    # mobile
    tel_type, code = get_teltype_and_codearea_of_number("93427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "9342")
    assert is_bangalore_area(code) == False

    tel_type, code = get_teltype_and_codearea_of_number("83427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "8342")
    assert is_bangalore_area(code) == False

    tel_type, code = get_teltype_and_codearea_of_number("73427 40118")
    assert (tel_type == TelTypes.mobile.value)
    assert (code == "7342")

    tel_type, code = get_teltype_and_codearea_of_number("23427 40118")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == "0", "expected=0, actual={}".format(code)

    # fixed_line
    tel_type, code = get_teltype_and_codearea_of_number("(04344)228249")
    assert (tel_type == TelTypes.fixed_line.value)
    assert code == "04344", "expected=04344, actual={}".format(code)
    assert is_bangalore_area(code) == False

    tel_type, code = get_teltype_and_codearea_of_number("(080)228249")
    assert (tel_type == TelTypes.fixed_line.value)
    assert code == "080", "expected=080, actual={}".format(code)
    assert is_bangalore_area(code) == True

    tel_type, code = get_teltype_and_codearea_of_number("(140)8371942")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == "0", "expected=0, actual={}".format(code)

    # telemarketer
    tel_type, code = get_teltype_and_codearea_of_number("1408371942")
    assert (tel_type == TelTypes.telemarketer.value)
    assert (code == "140")

    tel_type, code = get_teltype_and_codearea_of_number("14083 71942")
    assert (tel_type == TelTypes.not_valid.value)
    assert code == "0", "expected=0, actual={}".format(code)

    print("->test_get_teltype_and_codearea_of_number: is finished")


def test_get_fixed_line_area_code():
    print("---------------------------------------------")
    print("->get_fixed_line_area_code:start")
    assert (get_fixed_line_area_code("(04344)228249") == "04344")
    assert (get_fixed_line_area_code("(080)228249") == "080")
    assert (get_fixed_line_area_code("(080228249") != "080")
    print("->get_fixed_line_area_code: is finished")


def test_create_codes_dialed_by_bangalor_set_1():
    print("---------------------------------------------")
    print("->test_create_codes_dialed_by_bangalor_set_1:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "(034)78655", "1/9/2016  7:31", "15"],  # 034
                  ["(080)77777777", "(080)11111111", "1/9/2016  7:31", "15"],  # 080
                  ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],  # 9036
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(080)69245029", "1408371942", "1/9/2016  7:31", "15"]]  # 140
    create_codes_dialed_by_bangalor_set(calls_list)
    print("codes_dialed_by_bangalor_set=" + str(codes_dialed_by_bangalor_set))
    assert (len(codes_dialed_by_bangalor_set) == 4)

    expected_result = 1
    assert Amount.bangalor_responses == expected_result, \
        "Actual result= {}, expected result = {}".format(Amount.bangalor_responses, expected_result)

    expected_result = 4
    assert Amount.all_bangalor_calls == expected_result, \
        "Actual result= {}, expected result = {}".format(Amount.all_bangalor_calls, expected_result)

    assert (('034' in codes_dialed_by_bangalor_set) == True)
    assert (('8301' not in codes_dialed_by_bangalor_set) == True)
    assert (('9036' in codes_dialed_by_bangalor_set) == True)
    assert (('140' in codes_dialed_by_bangalor_set) == True)
    print("->test_create_codes_dialed_by_bangalor_set_1: is finished")


def test_create_codes_dialed_by_bangalor_set_2():
    print("---------------------------------------------")
    print("->test_create_codes_dialed_by_bangalor_set_2:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)44444444", "(080)78655", "1/9/2016  7:31", "15"],  # 080
                  ["(080)2222222", "(034)78655", "1/9/2016  7:31", "15"],  # 034
                  ["11111111111", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "(003)65 06212", "1/9/2016  7:31", "15"],  # 003
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"]]
    create_codes_dialed_by_bangalor_set(calls_list)
    print("codes_dialed_by_bangalor_set=" + str(codes_dialed_by_bangalor_set))
    assert (len(codes_dialed_by_bangalor_set) == 3)

    print("all_bangalor_calls={}, "
          "bangalor_responses={}".format(Amount.all_bangalor_calls, Amount.bangalor_responses))

    expected_result = 1
    assert Amount.bangalor_responses == expected_result, \
        "Actual result= {}, expected result = {}".format(Amount.bangalor_responses, expected_result)

    expected_result = 3
    assert Amount.all_bangalor_calls == expected_result, \
        "Actual result= {}, expected result = {}".format(Amount.all_bangalor_calls, expected_result)

    assert (('080' in codes_dialed_by_bangalor_set) == True)
    assert (('003' in codes_dialed_by_bangalor_set) == True)
    assert (('8301' not in codes_dialed_by_bangalor_set) == True)
    assert (('034' in codes_dialed_by_bangalor_set) == True)

    print("->test_create_codes_dialed_by_bangalor_set_2: is finished")


def test_calculate_percentage_1():
    print("---------------------------------------------")
    print("->test_calculate_percentage_1:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "(034)78655", "1/9/2016  7:31", "15"],  # 034
                  ["(080)77777777", "(080)11111111", "1/9/2016  7:31", "15"],  # 080
                  ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],  # 9036
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(04456)69245029", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(080)69245029", "1408371942", "1/9/2016  7:31", "15"]]  # 140
    create_codes_dialed_by_bangalor_set(calls_list)
    print("codes_dialed_by_bangalor_set= " + str(codes_dialed_by_bangalor_set))
    # 4 calls, 1 answers
    actual_result = calculate_percentage()
    expected_result = (1 * 100) / 4

    assert actual_result == expected_result, \
        "Actual result= {}, expected result = {}".format(actual_result, expected_result)

    print("->test_calculate_percentage_1: is finished")


def test_calculate_percentage_2():
    print("---------------------------------------------")
    print("->test_calculate_percentage_2:start")
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)44444444", "(034)78655", "1/9/2016  7:31", "15"],  # 034
                  ["(080)44444444", "(080)1111111111", "1/9/2016  7:31", "15"],  # 080
                  ["(080)44444444", "1403565656", "1/9/2016  7:31", "15"],  # 140
                  ["(080)2222222", "(034)78655", "1/9/2016  7:31", "15"],  # 034
                  ["11111111111", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "66666 6666", "1/9/2016  7:31", "15"],  # wrong format
                  ["(080)11111111", "(080)55555", "1/9/2016  7:31", "15"],  # 080
                  ["(080)11111111", "94567 4567", "1/9/2016  7:31", "15"],  # 9456
                  ["(080)11111111", "74567 4567", "1/9/2016  7:31", "15"],  # 7456
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"]]
    create_codes_dialed_by_bangalor_set(calls_list)
    print("codes_dialed_by_bangalor_set= " + str(codes_dialed_by_bangalor_set))
    # 8 calls, 2 answer
    actual_result = calculate_percentage()
    expected_result = (2 * 100) / 8

    assert actual_result == expected_result, \
        "Actual result= {}, expected result = {}".format(actual_result, expected_result)

    print("->test_calculate_percentage_2: is finished")


def test_get_sorted_codes_dialed_by_bangalor_set():
    print("---------------------------------------------")
    print("->test_get_sorted_codes_dialed_by_bangalor_set:start")
    calls_list = [["(080)44444444", "90365 06212", "1/9/2016  6:46:56 AM", "165"],  # 9036
                  ["(0843)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(0310)2222222", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(0334670)44444444", "(034)78655", "1/9/2016  7:31", "15"],
                  ["(09910)44444444", "66666 6666", "1/9/2016  7:31", "15"],
                  ["(080)44444444", "(084)44444444", "1/9/2016  7:31", "15"],  # 084
                  ["(080)55555555", "14044444444", "1/9/2016  7:31", "15"],  # 140
                  ["(080)55555555", "(080)44444444", "1/9/2016  7:31", "15"],  # 080
                  ["(081)55555555", "774554 4788", "1/9/2016  7:31", "15"],
                  ["(04456)333333", "(080)53227", "1/9/2016  7:31", "15"],
                  ["(04456)666666", "83019 53227", "1/9/2016  7:31", "15"],
                  ["(020)666666", "75674 53227", "1/9/2016  7:31", "15"]]
    create_codes_dialed_by_bangalor_set(calls_list)
    print("codes_dialed_by_bangalor_set= " + str(codes_dialed_by_bangalor_set))
    sorted_result = list(get_sorted_codes_dialed_by_bangalor_set())
    expected_result = ["080", "084", "140", "9036"]
    assert sorted_result == expected_result, \
        "expected={}, \n actual={}".format(expected_result, sorted_result)
    print("->test_get_sorted_codes_dialed_by_bangalor_set: is finished")


def test_get_2decimal_digits():
    print("---------------------------------------------")
    print("->test_get_2decimal_digits:start")
    actual_result = get_2decimal_digits(25)

    expected_result = "25.00"
    assert actual_result == expected_result, "actual_result={}, expected_result={}". \
        format(actual_result, expected_result)

    actual_result = get_2decimal_digits(25.5678)
    expected_result = "25.57"
    assert actual_result == expected_result, "actual_result={}, expected_result={}". \
        format(actual_result, expected_result)

    actual_result = get_2decimal_digits(0)
    expected_result = "0.00"
    assert actual_result == expected_result, "actual_result={}, expected_result={}". \
        format(actual_result, expected_result)

    actual_result = get_2decimal_digits(4.3333333333)
    expected_result = "4.33"
    assert actual_result == expected_result, "actual_result={}, expected_result={}". \
        format(actual_result, expected_result)
    print("->test_get_2decimal_digits: is finished")


def test():
    print("START ALL TESTS....")
    test_get_teltype_and_codearea_of_number()
    test_get_fixed_line_area_code()
    test_create_codes_dialed_by_bangalor_set_1()
    test_create_codes_dialed_by_bangalor_set_2()
    test_calculate_percentage_1()
    test_calculate_percentage_2()
    test_get_sorted_codes_dialed_by_bangalor_set()
    test_get_2decimal_digits()
    print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

# test()
main()
