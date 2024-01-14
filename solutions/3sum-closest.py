class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float("inf")

        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(target - curr_sum) < abs(target - close_sum):
                    close_sum = curr_sum
                    
                if curr_sum < target:
                    l+=1
                else:
                    r-=1
        return close_sum


