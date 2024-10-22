# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        res = 0
        for i in range(k):
            res += mx
            mx+=1
        return res
