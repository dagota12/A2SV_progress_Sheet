class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        n = len(nums)
        l,r = 0,len(nums) - 1
        best = 6000
        while l <= r:
            mid = l + (r - l)//2
            best = min(best,nums[mid])
            if nums[-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return best
