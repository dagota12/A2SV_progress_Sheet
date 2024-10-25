# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [(nums[i],i) for i in range(n)]
        arr.sort()

        min_index = n  
        max_width = 0

        for val,i in arr:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width