# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def is_palid(s):
            return s == s[::-1]
        n = len(s)
        memo = {}
        def dp(start):

            if start >= n:
                return 0
            if start not in memo:
                cut = float('inf')
                for i in range(start,n):
                    if is_palid(s[start:i+1]):
                        cut = min(cut,dp(i+1) + 1)
                memo[start] = cut
            return memo[start]
        return dp(0)-1
