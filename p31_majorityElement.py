"""
QUES: Majority Element
"""


# Time(N) Space(1) we are setting index 0 as answer if the next element is not the same as current then we will
# decrease count and if count become 0 somehow then the next index element will become the current ans and after
# itterating element of array we will check if count > len(array)//2 if  yes then its a ans or it will print none

def majority(arr):
    ansIndex = 0
    count = 1
    for i in range(len(arr)):
        if arr[i] == arr[ansIndex]:
            count += 1
        else:
            count -= 1
        if count == 0:
            ansIndex = i
            count = 1
    if len(arr) // 2 < count:
        return arr[ansIndex]


arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(majority(arr))
