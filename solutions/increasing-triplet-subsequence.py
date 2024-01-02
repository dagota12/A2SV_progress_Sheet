class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float("inf")
        b = float("inf")
        for i  in range(len(nums)):
            if nums[i] <= a:
                a = nums[i]
            elif nums[i] > a and nums[i] <= b:
                b = nums[i]
            elif nums[i] > a and nums[i] > b:
                return True