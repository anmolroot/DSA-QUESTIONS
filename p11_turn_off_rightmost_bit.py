"""
QUES: Turn off the rightmost set bit
"""


# Time Complexity: O(1)
# Auxiliary Space: O(1)


def fun(n):
    return n & (n - 1)


n = 12
print("The number after unsetting the rightmost set bit", fun(n))
