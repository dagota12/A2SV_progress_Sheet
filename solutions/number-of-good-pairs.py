class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1
        count = 0
        for val in freq.values():
            val = val-1
            count += (val*(val+1))//2
        return count

        