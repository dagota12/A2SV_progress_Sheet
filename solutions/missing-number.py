class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        for i in range(len(nums)+1):
            if not i in freq:
                return i