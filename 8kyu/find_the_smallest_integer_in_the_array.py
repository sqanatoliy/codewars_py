"""DESCRIPTION:
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""


def find_smallest_int(arr: int) -> int:
    # Code here
    min_num = arr[0]
    for number in arr:
        if number < min_num:
            min_num = number
    return min_num
