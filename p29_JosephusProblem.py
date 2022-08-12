"""
QUES: Josephus problem
"""


def jos(n, k):
    if n == 1:
        return 0
    return (jos(n - 1, k) + k) % n


# here n: total number of  mens in circular order
# here k: it mean the kth index person gonna die and gun is gonna passed to the k+1 men mean next person
n, k = 5, 3
print(jos(n, k))  # it return the index value of the man
