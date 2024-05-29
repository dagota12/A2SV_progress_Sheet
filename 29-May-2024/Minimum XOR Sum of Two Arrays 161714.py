# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        n = len(nums1)

        def backtrack(idx,mask):
            if (idx,mask) in memo:
                return memo[(idx,mask)]
            if idx >= n:
                return 0
            min_xor = float('inf')
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    res = (nums1[idx] ^ nums2[i]) + backtrack(idx+1,mask | (1<<i))
                    min_xor = min(min_xor,res)
            memo[(idx,mask)] = min_xor
            return memo[(idx,mask)]
        return backtrack(0,0)