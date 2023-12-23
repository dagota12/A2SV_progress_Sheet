class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res,c = 0,0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
            elif nums[i] == 0:
                res = max(res,c)
                c=0
        res = max(res,c)
        
        return res
