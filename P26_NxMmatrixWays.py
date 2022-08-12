"""
QUES: Number of ways in an NxM matrix
"""


# Approach base case is if we have only 1 row or 1 column the no. of ways to reach one point to another point is only 1
# so we will find the no.of ways for n-1 rows and m-1 column than we gonna add them

def matrix(n, m):
    if n == 1 or m == 1:
        return 1
    return matrix(n - 1, m) + matrix(n, m - 1)


n, m = 3, 3 # n = rows and m = column
print(matrix(n, m))
