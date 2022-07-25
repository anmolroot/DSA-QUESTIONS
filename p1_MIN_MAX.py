"""
QUES: Maximum and minimum of an array using minimum number of comparisons
METHOD 1 (Simple Linear Search)
"""


class Pair:
    def __init__(self):
        self.min = None
        self.max = None


# METHOD 1 (Simple Linear Search)
# In this method, the total number of comparisons is 1 + 2(n-2) in the worst case and 1 + n – 2 in the best case.
# In the above implementation, the worst case occurs when elements are sorted in descending order and the best case
# occurs when elements are sorted in ascending order.
# Time = O(1)
# space = O(1)
def getMinMax(arr: list, n: int) -> Pair:
    minmax = Pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax


# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
