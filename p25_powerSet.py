"""
QUES: Power Set
Note: no. of element in power set is 2^n where n is the number of elements in the set
"""

# Time(n2^n)
# Space(1)

# Method 1: iterative
import math


def printPowerSet(set, set_size):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = int(math.pow(2, set_size))

    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if (counter & (1 << j)) > 0:
                print(set[j], end="")
        print("")


set = ['a', 'b', 'c']
# printPowerSet(set, 3)


# Method 2: recursive
# Time(2^n)
# Space(1)

def powerSet(string, index, curr):
    if index == len(string):
        return print(curr)
    powerSet(string, index + 1, curr + string[index])
    powerSet(string, index + 1, curr)


string = "abc"
curr = ""
index = 0
print(powerSet(string, index, curr))
