"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
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

# my solution before resubmit
'''
incoming_number, answering_number, time, lasting_time_secs = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".
      format(incoming_number, answering_number, time, lasting_time_secs))
'''

'''
Don't agree about a comment:
    Its best practice to avoid using redundant variables when the calls 
    list already has the values and can be referred directly.
    It makes code look more redundant and noisy
    For Example
    print("Last record of calls {} calls {} at time {}lasting {} seconds".
    format(calls[-1][0],calls[-1][1],calls[-1][2],calls[-1][3]).

MY REASONING:
    If I need to debug my line of code it is quite convenient to see the variables as 
    answering_number and not calls[-1][1]. 
    Also I think that code looks way better with human readable format like answering_number instead of
    calls[-1][1]
    Even if Python allows to do a lot of things in 1 line it does not mean that it is convenient to debug
    or read or understand.
    
So it would be better to mark this as a SUGGESTION but NOT as REQUIRED 
'''

print("Last record of calls {} calls {} at time {}lasting {} seconds".
      format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
