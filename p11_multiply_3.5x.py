"""
QUES: Multiply a given Integer with 3.5
"""

# Time Complexity : O(1)
# Space Complexity : O(1)



def multiplyWith3Point5(x):
    # As we know 3.5x = (35/10)x or (7/2)x or (x + 2x + x/2)
    # for 2X we do left shift
    # for X/2 we do right shift
    return (x<<1) + x + (x>>1)


x = 4
print(multiplyWith3Point5(x))