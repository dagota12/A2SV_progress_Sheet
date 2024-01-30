class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        prefix = 0 
        for num in nums:
            prefix += num
            if prefix - goal in freq:
                count += freq[prefix - goal]
            freq[prefix] += 1
            
        return count