class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r,best = 1,max(nums),-1
        while l <= r:
            curr_div = l + (r-l)//2
            curr_sum = 0
            for num in nums:
                curr_sum += ceil(num/curr_div)
            if curr_sum <= threshold:
                r = curr_div - 1
                best = curr_div
            else:
                l = curr_div + 1
        return best