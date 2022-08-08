"""
QUES: FIND THE TRAILING NO. OF ZEROES
"""

# Time Complexity: O(log5n)
# Auxiliary Space: O(1)


def TrailingNoOfZeroes(num: int):
    count = 0
    i = 5
    while (num/i >= 1):
        count += (num//i)
        i *= 5
    return count


a = 25
print(TrailingNoOfZeroes(a))