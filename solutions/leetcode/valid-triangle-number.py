class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count,n = 0, len(nums)
        for i in range(n-1,0,-1):
            curr = nums[i]
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > curr:
                    count += r-l
                    r -= 1
                else:
                    l += 1
        return count


