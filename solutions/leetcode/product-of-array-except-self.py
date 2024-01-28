class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumulator = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i]  =  accumulator
            accumulator *= nums[i]
        
        accumulator = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= accumulator
            accumulator *= nums[i]
        return res
