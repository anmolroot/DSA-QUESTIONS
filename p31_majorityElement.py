"""
QUES: Majority Element
"""


# Time(N) Space(1) we are setting index 0 as answer if the next element is not the same as current then we will
# decrease count and if count become 0 somehow then the next index element will become the current ans and after
# itterating element of array we will check if count > len(array)//2 if  yes then its a ans or it will print none

def findCandidate(arr):
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
    return isMajority(arr, arr[ansIndex])

def isMajority(arr, candidate):
    count = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            count += 1
    if count > len(arr) // 2:
        return candidate
    else:
        return -1



arr = [3, 3, 4, 2, 4, 4, 2, 4]
print(isMajority(arr))

# Time(N)
# Space(N)
# HashMap Approach
def findMajority(arr, size):
    map = {}
    for i in range(size):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    count = 0
    for key in map:
        if map[key] > size/2:
            count = 1
            print(key)
            break
    if count == 0:
        return None


arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
n = len(arr)
findMajority(arr, n)


# Method 3: first sort then do count and check the max count check the element with max count if it is bigger than n//2
def majorityElement(arr, n):
    global element
    arr.sort()
    count = 1
    cur_max = -1
    temp_element = arr[0]
    flag = 0
    for i in range(1, n):
        if temp_element == arr[i]:
            count += 1
        else:
            count = 1
            temp_element = arr[i]

        if cur_max < count:
            cur_max = count
            element = arr[i]

            if cur_max > n//2:
                flag = 1
                break

    if flag == 1:
        return element
    else:
        return -1


arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)
print(majorityElement(arr, n))

