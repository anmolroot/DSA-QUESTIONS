"""QUES: Chocolate Distribution Problem
Given an array A[ ] of positive integers of size N, where each value
represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M
students, the task is to distribute chocolate packets among M students such that : 1. Each student gets exactly one
packet. 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates
given to a student is minimum. """


# METHOD 1
# Time = O(n)
# Space = O(1)
# https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1


class Solution:

    def findMinDiff(self, A, N, M):
        ans = float('inf')
        A.sort()
        first_min_student = 0
        last_max_student = M - 1
        while last_max_student < N:
            min_ans = min(ans, A[last_max_student] - A[first_min_student])
            first_min_student += 1
            last_max_student += 1
        return min_ans
