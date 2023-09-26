"""DESCRIPTION:
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    lst_words = s.split(" ")
    l = lst_words[0]
    for word in lst_words:
        if len(word) < len(l):
            l = word
    # your code here
    return len(l)  # l: shortest word length
