# TASK
'''
In this first exercise, the goal is to write a function that takes a string as input and then returns
the reversed string.

For example, if the input is the string "water", then the output should be "retaw".

While you're working on the function and trying to figure out how to manipulate the string,
it may help to use the print statement so you can see the effects of whatever you're trying.

Note - You can use built-in method len() on the string.

'''


# Code

def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    result = ""
    # TODO: Write your solution here
    for i in range(len(our_string)):
        result += our_string[(len(our_string) - 1) - i]
        print("result=" + result + ", i=" + str(i))
    return result

    pass


# Test Cases

print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
