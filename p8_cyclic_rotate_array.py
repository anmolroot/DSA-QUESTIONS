"""
QUES: Cyclically rotate an array by one
Given an array, rotate the array by one position in clock-wise direction.
"""


# METHOD 1
# TIME = O(n)
# Space = O(1)
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

# User function Template for python3
def rotate(arr, n):
    temp = 0
    for i in range(n):
        temp = arr[i]
        arr[i] = arr[n - 1]
        arr[n - 1] = temp
    return arr
