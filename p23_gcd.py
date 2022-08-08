"""
QUES: GCD OR HCF OF TWO NUMBER
"""


# Method 1
def GCD(num1, num2):
    ans = 0
    while num2!=0:
        if num1 > num2:
            ans = num1 % num2
            num1, num2 = num2, ans
    return num1

if __name__ == '__main__':
    print(GCD(42, 24))



