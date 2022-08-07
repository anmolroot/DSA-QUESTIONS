"""
QUES: Python3 code to add one to a given number
"""

# Time Complexity: O(log2n)
# Auxiliary Space: O(1)


def addOne(x):
    m = 1;
    # Flip all the set bits
    # until we find a 0
    while (x & m):
        x = x ^ m
        m <<= 1

    # flip the rightmost
    # 0 bit
    x = x ^ m
    return x

n = 199
print(addOne(n))