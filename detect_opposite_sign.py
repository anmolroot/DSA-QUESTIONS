"""
QUES: Detect if two integers have opposite signs
"""


def oppositeSigns(x, y):
    return (x ^ y) < 0


x = int(input("input any integer digit"))
y = int(input("input any integer digit"))
print(oppositeSigns(x, y))
