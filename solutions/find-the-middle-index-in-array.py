class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        for i in range(len(nums)):
            left = nums[i-1] if i > 0 else 0
            right = nums[-1] - nums[i] 
            if right == left:
                return i
        return -1
