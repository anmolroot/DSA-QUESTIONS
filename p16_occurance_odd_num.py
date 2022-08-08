"""
QUES: Given an array of positive integers. All numbers occur an even number of times except one number which occurs an
 odd number of times. Find the number in O(n) time & constant space.
"""

# Method 1
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

def getOddOccurrence(arr, arr_size):
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]
    return -1


arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
n = len(arr)
print(getOddOccurrence(arr, n))

# Method 2
# Time Complexity: O(n)
# Auxiliary Space: O(n)

def getOddOccurrence(arr, size):
    Hash = dict()
    for i in range(size):
        Hash[arr[i]] = Hash.get(arr[i], 0) + 1

    for i in Hash:
        if Hash[i] % 2 != 0:
            return i
    return -1


arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
n = len(arr)

print(getOddOccurrence(arr, n))
