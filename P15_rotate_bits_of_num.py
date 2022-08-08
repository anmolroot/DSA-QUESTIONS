"""
QUES: Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the bits that fall off
at one end are put back to the other end.
In left rotation, the bits that fall off at left end are put back at right end.
In right rotation, the bits that fall off at right end are put back at left end.
"""

# Time Complexity: O(1)
# Auxiliary Space: O(1)


INT_BITS = 32


def leftRotate(x, d):
    return x << d | x >> (INT_BITS - d)


def rightRotate(x, d):
    return x >> d | (x << (INT_BITS - d)) & 0xFFFFFF


n = 16
d = 2

print("Left Rotation of", n, "by"
      , d, "is", end=" ")
print(leftRotate(n, d))

print("Right Rotation of", n, "by"
      , d, "is", end=" ")
print(rightRotate(n, d))
