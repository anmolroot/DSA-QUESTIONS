"""
QUES: Power using Recursion
"""


# Approach: f(base,exp) = f(base, exp - 1) * base

def powerRecursion(given_base, given_exp):
    if given_exp == 1:
        return given_base

    if given_exp != 1:
        return given_base * powerRecursion(given_base, given_exp - 1)


given_base = 4
given_exp = 11
# passing the given base an exponent as arguments to the recursive function powerRecursion
print(given_base, "^", given_exp, ' = ', powerRecursion(given_base, given_exp))
