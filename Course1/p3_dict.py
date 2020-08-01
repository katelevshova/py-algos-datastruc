"""
Read file into texts and calls.
"""

import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds,
on the phone during September 2016.".
"""

telnumbers_calltime_dict = dict()

'''
Creates a dictionary where key = tel_number and value = the total duration in seconds
spent on incoming and outgoing calls for a specific time period.
ARGS:
    calls_list (list) - list of lists. Example:
                    [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                    ["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"]]
    period_month and period_year (tuple of int)
'''


def create_telnumbers_dict_for_period(calls_list, period_month, period_year):
    # print("->create_telnumbers_dict_for_period: for period month={}, year={}".format(period_month, period_year))
    telnumbers_calltime_dict.clear()

    for call in calls_list:
        # 27-09-2016 21:22:34, 1/9/2016  6:01:12 AM
        only_date_from_str = call[2].split(" ")[0]
        date = get_date(only_date_from_str)
        # print("date={}, date.year={}, date.month={}".format(date, date.year, date.month))
        if date is not None and date.year == period_year and date.month == period_month:
            outgoing_number = call[0]
            incoming_number = call[1]
            # print("outgoing_number = {}, incoming_number= {}".format(outgoing_number, incoming_number))
            call_duration = int(call[3])
            check_dictionary(outgoing_number, call_duration)
            check_dictionary(incoming_number, call_duration)


'''
Creates a dictionary where key = tel_number and value = the total duration in seconds
spent on incoming and outgoing calls.
ARGS:
    tel_number (string) in any format.
        Example: input tel_number="(080)46304537" would be converted to "08046304537" and used as a key
                 input tel_number="99003 47921" would be converted to "9900347921" and used as a key
    call_duration (int) in seconds
'''


def check_dictionary(tel_number, call_duration):
    only_digits_tel_number = ''.join(filter(lambda i: i.isdigit(), tel_number))
    # print("tel_number= {}, only_digits_tel_number = {}".format(tel_number, only_digits_tel_number))
    telnumbers_calltime_dict[only_digits_tel_number] = telnumbers_calltime_dict.get(
        only_digits_tel_number, 0) + call_duration


'''
Returns a date object based on the given date string in two formats day-month-year and day/month/year
ARGS:
    datetime_str (string) Example_1: 27-09-2016 Example_2: 1/9/2016
'''


def get_date(datetime_str):
    # We assume that all dates are in european style format - day, month, year
    date_patterns = ["%d/%m/%Y", "%d-%m-%Y"]
    for pattern in date_patterns:
        try:
            return datetime.strptime(datetime_str, pattern).date()
        except ValueError as value_error:
            # print('ValueError Raised:', value_error)
            pass
    print("Date is not in expected format: {}".format(datetime_str))


'''
Returns a tuple of telephone number and its call time duration which is the maximum
among all items in the dictionary
Example: "9900347921", 1689
'''


def get_telnumber_with_max_calltime():
    max_duration = 0
    result_number = ""
    for key, value in telnumbers_calltime_dict.items():
        if value > max_duration:
            max_duration = value
            result_number = key
    return (result_number, max_duration)


'''
Returns the full month name based on the months number
ARGS:
    month_number (int)
EXAMPLE: it will return September if month_number is equal 9
'''


def get_full_month_name(month_number):
    datetime_object = datetime.strptime(str(month_number), "%m")
    return datetime_object.strftime("%B")


def main():
    period_month, period_year = (9, 2016)
    create_telnumbers_dict_for_period(calls, period_month, period_year)

    tel_number_result, max_duration = get_telnumber_with_max_calltime()
    month_name_full_str = get_full_month_name(period_month)
    # print("datetime_object="+str(datetime_object)+", month_name_full_str= "+str(month_name_full_str))

    print("{} spent the longest time, {} seconds, on the phone during {} {}.".format
          (tel_number_result, max_duration, month_name_full_str, period_year))


# TEST CASES----------------------------------------------
def test_tel_numb_1():
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "83019 53227", "1/9/2016  7:31", "15"]]
    period_month, period_year = (9, 2016)
    create_telnumbers_dict_for_period(calls_list, period_month, period_year)
    tel_number_result, max_duration = get_telnumber_with_max_calltime()

    assert (tel_number_result == "7813000821")
    assert (max_duration == 165)
    # print("->test_tel_numb_1: Test finished")


def test_tel_numb_2():
    calls_list = [["78130 00821", "90365 06212", "1/9/2016  6:46:56 AM", "165"],
                  ["(080)69245029", "90365 06212", "1/9/2016  7:31", "15"],
                  ["(080)69245029", "90365 06212", "1/4/2016  7:31", "15"]]
    period_month, period_year = (9, 2016)
    create_telnumbers_dict_for_period(calls_list, period_month, period_year)
    tel_number_result, max_duration = get_telnumber_with_max_calltime()

    assert (tel_number_result == "9036506212")
    assert (max_duration == (165 + 15))
    # print("->test_tel_numb_2: Test finished")


def test_get_full_month_name():
    assert (get_full_month_name(9) == "September")
    assert (get_full_month_name(3) == "March")
    # print("->test_get_full_month_name: Test finished")


def test():
    test_tel_numb_1()
    test_tel_numb_2()
    test_get_full_month_name()
    # print("ALL TESTS FINISHED....")


# ----------------------------------------------------------

# test()
main()
