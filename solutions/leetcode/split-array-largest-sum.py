class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r,best = max(nums),sum(nums),-1
        while l <= r:
            mid = l + (r-l)//2
            sum_ = 0
            parts = 1
            
            for i in range(len(nums)):
                sum_ += nums[i]
                if sum_ > mid:
                    parts += 1
                    sum_ = nums[i]
            if parts <= k:
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best