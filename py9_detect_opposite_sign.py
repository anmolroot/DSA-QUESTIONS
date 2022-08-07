"""
QUES: Detect if two integers have opposite signs
"""
# XOR gives 1 only on different bits
# if sign bit is 1: Negative
# if sign bit is 0: Positive

def oppositeSigns(x, y):
    return (x ^ y) < 0


x = int(input("input any integer digit"))
y = int(input("input any integer digit"))
print(oppositeSigns(x, y))
