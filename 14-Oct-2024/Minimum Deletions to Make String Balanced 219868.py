# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count,ct = [0]*n,0
        for i in range(n-1,-1,-1):
            a_count[i] = ct
            if s[i] == 'a': ct += 1
        removed = n
        b_count = 0
        for i in range(n):
            removed = min(removed,a_count[i] + b_count)
            if s[i] == 'b': b_count += 1
        return removed