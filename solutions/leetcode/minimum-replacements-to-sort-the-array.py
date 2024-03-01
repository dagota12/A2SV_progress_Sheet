class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                continue
            parts =  nums[i]//nums[i+1] + (1 if nums[i] % nums[i+1] else 0)
            nums[i] = nums[i]//parts
            count += parts - 1
        return count