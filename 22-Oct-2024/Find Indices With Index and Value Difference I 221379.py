# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], idxDiff: int, valDiff: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+idxDiff,n):
                if abs(nums[i] - nums[j]) >= valDiff:
                    return [i,j]
        return [-1,-1]