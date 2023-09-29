"""DESCRIPTION:
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
"""


def zero(operation=None):
    if operation:
        if operation[0] == "plus":
            return 0 + int(operation[1])
        if operation[0] == "minus":
            return 0 - int(operation[1])
        if operation[0] == "times":
            return 0 * int(operation[1])
        if operation[0] == "divided_by":
            return 0 // int(operation[1])
    return 0


def one(operation=None):
    if operation:
        if operation[0] == "plus":
            return 1 + int(operation[1])
        if operation[0] == "minus":
            return 1 - int(operation[1])
        if operation[0] == "times":
            return 1 * int(operation[1])
        if operation[0] == "divided_by":
            return 1 // int(operation[1])
    return 1


def two(operation=None):
    if operation:
        if operation[0] == "plus":
            return 2 + int(operation[1])
        if operation[0] == "minus":
            return 2 - int(operation[1])
        if operation[0] == "times":
            return 2 * int(operation[1])
        if operation[0] == "divided_by":
            return 2 // int(operation[1])
    return 2


def three(operation=None):
    if operation:
        if operation[0] == "plus":
            return 3 + int(operation[1])
        if operation[0] == "minus":
            return 3 - int(operation[1])
        if operation[0] == "times":
            return 3 * int(operation[1])
        if operation[0] == "divided_by":
            return 3 // int(operation[1])
    return 3


def four(operation=None):
    if operation:
        if operation[0] == "plus":
            return 4 + int(operation[1])
        if operation[0] == "minus":
            return 4 - int(operation[1])
        if operation[0] == "times":
            return 4 * int(operation[1])
        if operation[0] == "divided_by":
            return 4 // int(operation[1])
    return 4


def five(operation=None):
    if operation:
        if operation[0] == "plus":
            return 5 + int(operation[1])
        if operation[0] == "minus":
            return 5 - int(operation[1])
        if operation[0] == "times":
            return 5 * int(operation[1])
        if operation[0] == "divided_by":
            return 5 // int(operation[1])
    return 5


def six(operation=None):
    if operation:
        if operation[0] == "plus":
            return 6 + int(operation[1])
        if operation[0] == "minus":
            return 6 - int(operation[1])
        if operation[0] == "times":
            return 6 * int(operation[1])
        if operation[0] == "divided_by":
            return 6 // int(operation[1])
    return 6


def seven(operation=None):
    if operation:
        if operation[0] == "plus":
            return 7 + int(operation[1])
        if operation[0] == "minus":
            return 7 - int(operation[1])
        if operation[0] == "times":
            return 7 * int(operation[1])
        if operation[0] == "divided_by":
            return 7 // int(operation[1])
    return 7


def eight(operation=None):
    if operation:
        if operation[0] == "plus":
            return 8 + int(operation[1])
        if operation[0] == "minus":
            return 8 - int(operation[1])
        if operation[0] == "times":
            return 8 * int(operation[1])
        if operation[0] == "divided_by":
            return 8 // int(operation[1])
    return 8


def nine(operation=None):
    if operation:
        if operation[0] == "plus":
            return 9 + int(operation[1])
        if operation[0] == "minus":
            return 9 - int(operation[1])
        if operation[0] == "times":
            return 9 * int(operation[1])
        if operation[0] == "divided_by":
            return 9 // int(operation[1])
    return 9


def plus(number):
    return "plus", number


def minus(number):
    return "minus", number


def times(number):
    return "times", number


def divided_by(number):
    return "divided_by", number


if __name__ == "__main__":
    print(nine(divided_by(nine())))
