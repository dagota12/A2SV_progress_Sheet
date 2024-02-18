class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distnict = len(set(nums))
        frequency = defaultdict(int)
        left = 0
        subarrays = 0
        for right in range(len(nums)):
            frequency[nums[right]] += 1
            
            while len(frequency) == distnict:
                
                subarrays += len(nums)-right
                frequency[nums[left]] -= 1
                if frequency[nums[left]] == 0:
                    del frequency[nums[left]]
                left += 1
               
        return subarrays