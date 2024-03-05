class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subsets(idx=0,ans =[]):
            # print(idx,ans)
            if idx >= len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[idx])
            subsets(idx+1)
            ans.pop()
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            subsets(idx+1)
        subsets()
        return res