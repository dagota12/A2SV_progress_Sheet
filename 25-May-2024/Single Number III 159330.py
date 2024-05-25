# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor  = 0
        for num in nums:
            xor ^= num
        group1,group2 = 0, 0
        last_setbit = (xor & xor-1)^xor

        for num in nums:
            if num & last_setbit == 0:
                group1 ^= num
            else:
                group2 ^= num
        return [group1,group2]