"""You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""

def litres(time):
    return int(time//2)


if __name__=="__main__":
    print(litres(11.8))