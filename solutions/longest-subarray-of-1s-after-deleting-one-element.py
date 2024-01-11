class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_len = 1
        l = 0
        frequency_counter = defaultdict(int)
        for r in range(len(nums)):
            if nums[r] in frequency_counter:
                frequency_counter[nums[r]] += 1
                while nums[r] == 0 and frequency_counter[nums[r]] > 1:
                    frequency_counter[nums[l]] -= 1
                    l+=1
            else:
                frequency_counter[nums[r]] += 1
            max_len = max(max_len,r-l+1)
        return max_len-1

