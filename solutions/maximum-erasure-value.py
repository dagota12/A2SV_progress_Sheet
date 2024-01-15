class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        l = 0
        sum_ = 0
        ans = 0
        for r in range(len(nums)):
            frequency[nums[r]] += 1
            while frequency[nums[r]] > 1:
                frequency[nums[l]] -= 1
                sum_ -= nums[l]
                l+=1
            sum_ += nums[r]
            ans = max(ans,sum_)
        return ans
        
