"""
DESCRIPTION:
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1**2 + 2**2 + 2**2 = 9.
"""

def square_sum(numbers):
#     square_sum = []
#     total = 0
#     for number in numbers:
#         square_sum.append(number * number)
#     for square_num in square_sum:
#         total += square_num
#     return total
    return sum(i*i for i in numbers)
    #your code here
