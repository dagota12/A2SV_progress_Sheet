class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def perm(nums,choosen = set(),ans =[]):
            
            if len(nums) == len(ans):
                results.append(ans.copy())
                return 

            for i in range(len(nums)):
                if i in choosen:
                    continue
                ans.append(nums[i])
                choosen.add(i)
                perm(nums,choosen,ans)
                ans.pop()
                choosen.remove(i)
        perm(nums)
        return results