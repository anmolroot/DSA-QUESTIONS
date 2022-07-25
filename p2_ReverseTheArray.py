"""
QUES: Write a program to reverse an array or string
"""

"""
METHOD:1 --> ITERATIVE WAY
Time = O(n)
Space = (1)
"""


def reverseList(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    start = 0
    end = len(arr) - 1
    print(reverseList(arr, start, end))

"""
METHOD:2 --> RECURSIVE WAY
Time = O(n)
Space = (1)
"""


def reverseList(arr, start, end):
    if start > end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    reverseList(arr, start + 1, end - 1)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    start = 0
    end = len(arr) - 1
    print(reverseList(arr, start, end))
