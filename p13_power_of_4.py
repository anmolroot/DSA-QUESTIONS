"""
QUES: Given a number N, check if N is power of 4 or not.
"""

# Time Complexity: O(log4n)
# Auxiliary Space: O(1)

class Solution():
    def isPowerofFour(self, n):
         # code here
        self.temp = 1
        if n == 1 or n == 0:
            return n
        while self.temp <= n:
            if self.temp == n:
                return 1
            else:
                self.temp *= 4
        return 0