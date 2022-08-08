"""
QUES:Write an efficient program to count the number of 1s in the binary representation of an integer.
"""

# method 1 (iterative)
# Time Complexity: O(logn)
# Auxiliary Space: O(1)


def countSetBits(n):
    count = 0
    while n:
        count += (n & 1)
        n >> 1
    return count


i = 9
print(countSetBits(i))

# Method 2 (Recursive)

def countSetBits(n):
    if n == 0:
        return 0
    return (n & 1) + countSetBits(n >> 1)


n = 9
print(countSetBits(n))



