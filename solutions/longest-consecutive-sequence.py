class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                ct = 1
                while y in nums:
                    y += 1
                    ct += 1
                best = max(best, ct)
        return best