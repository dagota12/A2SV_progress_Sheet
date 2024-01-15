class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        max_ = 0
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while nums[r] == 0 and freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l+=1
            max_ = max(max_,r - l + 1)
        return max_


