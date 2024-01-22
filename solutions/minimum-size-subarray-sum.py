class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_ = 10**5+1
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_ = min(min_,r - l + 1)
                curr_sum -= nums[l]
                l+=1
        return 0 if min_ > 10**5 else min_
