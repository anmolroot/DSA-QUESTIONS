"""
QUES: KADANES ALGO OR MAX SUB ARRAY
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.A subarray is a contiguous part of an array.
"""


# https://leetcode.com/problems/maximum-subarray/
# Time = O(n)
# Space = O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if there is only 1 element then the first element is the max element
        max_sum = nums[0]

        # we use cur_sum to add every consecutive element to get max consecutive subarray
        cur_sum = 0

        # we gonna iterate through  every element so that we can sum them
        for i in nums:

            # this is a special condition to check if the first element is negative or not and also.
            # it gonna help in future cu_sum if its negative then we can make to zero to our max_sumdo not change
            if cur_sum < 0:
                cur_sum = 0

            # we are adding the consicutive element
            cur_sum += i

            # here we are storing max sub array sum to max_sum
            max_sum = max(cur_sum, max_sum)

        return max_sum
