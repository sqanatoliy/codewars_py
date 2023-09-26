"""DESCRIPTION:
In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

Good luck!

Please also try Simple remove duplicates"""

def solve(strng: str) -> list:
    final_list = []
    dig_list = []
    for i in strng:
        if i.isdigit():
            dig_list.append(i)
        else:
            dig_list.append(" ")
    for i in "".join(dig_list).split():
        final_list.append(int(i))
    largest = 0
    for i in final_list:
        if i > largest:
            largest = i
    return largest