class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        for i,num in enumerate(nums):
            if i > curr:
                return False
            curr = max(curr,i + num)
        return True