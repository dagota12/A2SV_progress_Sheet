class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        curr_max = 0
        for i in range(len(nums)):
            curr_max = max(curr_max,0)
            curr_max += nums[i]
            max_ = max(max_,curr_max)
        return max_
