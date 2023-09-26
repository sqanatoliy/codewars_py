"""DESCRIPTION:
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]"""

def digitize(n):
    number_str = str(n)
    digit_list = [int(digit) for digit in number_str]
    return digit_list[::-1]