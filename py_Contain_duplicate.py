"""
QUES: CONTAIN DUPLICATE
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


# https://leetcode.com/problems/contains-duplicate/
# Approach: HashSet
# Time = O(n)
# Space = O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            else:
                hashSet.add(i)

