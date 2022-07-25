"""
QUES: Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
"""


# https://leetcode.com/problems/find-the-duplicate-number/
# Approach: HashSet
# Time = O(n)
# Space = O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return i
            else:
                hashSet.add(i)