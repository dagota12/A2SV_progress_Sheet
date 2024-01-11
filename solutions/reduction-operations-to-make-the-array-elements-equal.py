class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == nums[i+1]:
                continue
            count += len(nums) - 1 - i
        return count
             
