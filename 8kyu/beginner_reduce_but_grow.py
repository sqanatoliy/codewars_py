"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""


def grow(arr):
    product=1
    for i in arr:
        product *= i
    return product


if __name__=="__main__":
    print(grow([1, 2, 3]))