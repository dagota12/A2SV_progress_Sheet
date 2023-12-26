class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        for op in operations:
            t,v = op
            idx = mp[t]
            nums[idx] = v
            mp[v] = idx
        return nums