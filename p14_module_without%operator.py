"""
QUES: Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number. 
"""

# Time Complexity: O(1)
# As we are doing single operation which takes constant time.
# Auxiliary Space: O(1)


def getModulo(n, d):
    return (n & (d - 1))


n = 6

# d must be a power of 2
d = 4
print(n, "modulo", d, "is",
      getModulo(n, d))
