# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        ans = nums[-4] - nums[0]
        p1,p2 = 0,-4
        for i in range(4):
            ans = min(ans,nums[p2] - nums[p1])
            p1 += 1
            p2 += 1
        return ans