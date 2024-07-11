# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        mx = 0
        for i in range(1,n):
            mx = max(mx, nums[i] - nums[i-1])
        return mx