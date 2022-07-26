"""
QUES: Sort an arrray of 0s, 1s and 2s
"""

# METHOD 1
# Time = O(n)
# Space = O(1)
# CONS: This solution may not work if values are a part of the structure. For example, consider a situation
# where 0 represents Computer Science Stream, 1 represents Electronics and 2 represents Mechanical.
# We have a list of student objects (or structures) and we want to sort them.
# We cannot use the above sort as we simply put 0s, 1s, and 2s one by one.


# User function Template for python3

class Solution:
    def sort012(self,arr,n):
        count0 = 0
        count1 = 0
        count2 = 0
        for i in arr:
            if i == 0:count0 += 1
            if i == 1:count1 += 1
            if i == 2:count2 += 1

        for i in range(count0):arr[i] += 0
        for i in range(count0, (count0 + count1)):arr[i] += 1
        for i in range((count0 + count1), n):arr[i] += 2

        return arr

# METHOD 2
# Time = O(n)
# Space = O(1)
# Pros: Optimal Solution that handles above issues

inputArray = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
outputArray = []
indexOfZero = 0

for value in inputArray:
    if value == 0:
        outputArray.insert(0, value)
        indexOfZero += 1
    if value == 1:
        outputArray.insert(indexOfZero, value)
        indexOfZero += 1
    if value == 2: outputArray.append(value)

print(outputArray)
