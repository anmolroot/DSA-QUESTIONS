"""
QUES: sieve of Eratosthenes
"""




# method 1: little bit more effecient bcz we are marking false i**1
def sevOfEratos(n):
    if n == (1 or 0):
        return 0
    prime = [0, 0] + [True] * (n - 2)
    for i in range(2, int(n ** 0.5)):
        if prime[i] is True:
            for j in range(i ** i, len(prime), i):
                prime[j] = False





# method 2: less effecient bcz we are marking false of multiple of 2*i
def sevOfEratos(n):
    if n == (1 or 0):
        return 0
    prime = [0, 0] + [True] * (n - 2)
    for i in range(2, int(n ** 0.5)):
        if prime[i] is True:
            for j in range(2 * i, len(prime), i):
                prime[j] = False
    for k in range(len(prime)):
        if prime[k] == True:
            print(k)
    return

n = 1000
print(sevOfEratos(n))