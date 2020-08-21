"""
((32+8)∗(5/2))/(2+6).
Take a string as an input and return True if it's parentheses are balanced or False if it is not.
"""


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        """
        Adds item to the end
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last value
        """
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation_str):
    print(equation_str)
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()

    for char in equation_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False

    if stack.size() == 0:
        return True
    else:
        return False


def test_case_1():
    actual_result = equation_checker("((32+8)∗(5/2))/(2+6).")
    assert actual_result


def test_case_2():
    actual_result = equation_checker("()(()) ))))))).")
    assert actual_result == False


def test_case_3():
    actual_result = equation_checker("())((")
    assert actual_result == False


def test():
    test_case_1()
    test_case_2()
    test_case_3()


test()
