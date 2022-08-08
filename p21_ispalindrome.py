"""
QUES: IS GIVEN NUMBER PALIONDROME OR NOT
"""


def isPalindrome(num):
    result = 0
    temp = num
    while temp != 0:
        digit = temp % 10
        result = result * 10 + digit
        temp = temp // 10
    if result == num:
        return True
    else:
        return False


a = 404
print(isPalindrome(a))
