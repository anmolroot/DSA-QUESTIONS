"""
QUES: Trapping Rainwater
"""


def TrappingRainwater(arr, n):
    leftMax = [0] * n
    rightMax = [0] * n
    ans = 0
    # first set left most and the right most value as the max values
    leftMax[0] = arr[0]
    rightMax[n - 1] = arr[ n - 1]

    # Now we gonna fill it with max values of left side arr
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i])
    # Now we gonna fill it with max values of ride side arr
    for i in range(n-2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])

    # Now we will compare the parallel values of two array then we will get the minimum of two values for every index
    # and then i will subtract the current index value of array from the minimum then add this result untill the end of
    # array
    for i in range(n):
        ans += min(leftMax[i], rightMax[i]) - arr[i]
    return ans

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print(TrappingRainwater(arr, n))
