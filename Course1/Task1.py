"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_tel_numbers = set()

'''
Creates a set of telephone numbers based on the provided list of data.
ARGS:
	list_from_file (list) - data from the file
	The text data (text.csv) has the following columns (3): 
	0 - sending telephone number (str), 1 - receiving telephone number (str), 2 - timestamp of text message (str).
	The call data (call.csv) has the following columns (4):
	0 - calling telephone number (str), 1 - receiving telephone number (str), 
	2 - start timestamp of telephone call (string), 3 - duration of telephone call in seconds (string)
'''


def count_unique_telephone_number(list_from_file):
    for item in list_from_file:
        sending_number = ''.join(filter(lambda i: i.isdigit(), item[0]))
        receiving_number = ''.join(filter(lambda i: i.isdigit(), item[1]))
        # print("Sending number = {}, receiving number = {}".format(sending_number, receiving_number))
        unique_tel_numbers.add(sending_number)
        unique_tel_numbers.add(receiving_number)


count_unique_telephone_number(texts)
# print("--------------TEXTS----------------------------------")
# print("unique_tel_numbers="+str(unique_tel_numbers))
# print("length of a set unique_tel_numbers= "+str(len(unique_tel_numbers)))

count_unique_telephone_number(calls)
# print("--------------CALLS----------------------------------")
# print("unique_tel_numbers="+str(unique_tel_numbers))
# print("length of a set unique_tel_numbers= "+str(len(unique_tel_numbers)))

print("There are {} different telephone numbers in the records.".format(len(unique_tel_numbers)))
