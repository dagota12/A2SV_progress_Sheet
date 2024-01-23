class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        for num in nums:
            if num%2==1:
                prefix += 1
            count += freq[prefix-k]
            freq[prefix]+=1
        return count


