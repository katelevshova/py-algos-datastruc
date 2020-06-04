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
unique_texts_numbers = set()

def count_unique_telephone_number(list_from_file):
	for item in list_from_file:
		sending_number = ''.join(filter(lambda i: i.isdigit(), item[0]))
		receiving_number = ''.join(filter(lambda i: i.isdigit(), item[1]))
		#print("Sending number = {}, receiving number = {}".format(sending_number, receiving_number))
		
		if sending_number not in unique_texts_numbers:
			unique_texts_numbers.add(sending_number)
		if receiving_number	not in unique_texts_numbers:
			unique_texts_numbers.add(receiving_number)

count_unique_telephone_number(texts)
#print("--------------TEXTS----------------------------------")
#print("unique_texts_numbers="+str(unique_texts_numbers))
#print("length of a set unique_texts_numbers= "+str(len(unique_texts_numbers)))

count_unique_telephone_number(calls)
#print("--------------CALLS----------------------------------")
#print("unique_texts_numbers="+str(unique_texts_numbers))
#print("length of a set unique_texts_numbers= "+str(len(unique_texts_numbers)))

print("There are {} different telephone numbers in the records.".format(len(unique_texts_numbers)))