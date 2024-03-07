class Solution:
    def bisect(self,nums,target,left = True):
        idx = -1
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                idx = mid
            if left:
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return idx

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return (self.bisect(nums,target),self.bisect(nums,target,False))