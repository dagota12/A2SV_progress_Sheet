class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0: 
                nums[l] = nums[r]
                nums[r] = 0
            if nums[l] != 0:
                l+=1
            r+=1


            
        """
        Do not return anything, modify nums in-place instead.
        """
        