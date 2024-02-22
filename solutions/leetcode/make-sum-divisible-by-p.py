class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        rem = sum(nums)%p
        if not rem:
            return 0
        res = n
        prefix_sum = 0
        freq = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            key = (prefix_sum%p - rem)%p
            if key in freq:
                res = min(res, i-freq[key])
            freq[prefix_sum%p] = i
        return res if res < n else -1