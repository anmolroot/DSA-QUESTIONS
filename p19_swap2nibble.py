"""
QUES: A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.
Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte (or 8 bits).
 The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.
"""


def swapNibbles(x):
    return ((x & 0x0F) << 4 | (x & 0xF0) >> 4)


x = 100
print(swapNibbles(x))

# Explaination: 100 is 01100100 in binary. The operation can be split mainly in two parts
# 1) The expression “x & 0x0F” gives us last 4 bits of x. For x = 100, the result is 00000100.
# Using bitwise ‘<<‘ operator, we shift the last four bits to the left 4 times and make the new last four bits as 0.
# The result after shift is 01000000.
# 2) The expression “x & 0xF0” gives us first four bits of x. For x = 100, the result is 01100000.
# Using bitwise ‘>>’ operator, we shift the digit to the right 4 times and make the first four bits as 0.
# The result after shift is 00000110.