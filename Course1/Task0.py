"""
Read file into texts and calls.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # print("texts= " + str(texts))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # print("calls= " + str(calls))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
incoming_number, answering_number, time = texts[0]
print("First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time))

incoming_number, answering_number, time, lasting_time_secs = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".
      format(incoming_number, answering_number, time, lasting_time_secs))
'''
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".
      format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
'''