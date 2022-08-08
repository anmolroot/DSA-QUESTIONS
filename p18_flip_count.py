"""
QUES: Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
"""


def countFlips(a, b):
    flip = 0
    while (a > 0) or (b > 0):
        val1 = a & 1
        val2 = b & 1
        if (val1 != val2):
            flip += 1
        a >>= 1
        b >>= 1
    return flip


a = 10
b = 20
print(countFlips(a, b))
