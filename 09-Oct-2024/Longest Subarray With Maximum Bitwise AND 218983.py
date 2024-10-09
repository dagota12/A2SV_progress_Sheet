# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ct = lg = 0
        for num in nums:
            if num != mx:
                lg = max(lg,ct)
                ct = 0
            else:
                ct += 1
        lg = max(lg,ct)
        return lg
        