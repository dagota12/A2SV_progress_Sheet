class Solution:
    def subsets(self, nums1: List[int]) -> List[List[int]]:
        results = set()

        def subs(nums,l=0,ans=[]):
            if len(nums)  < 1:
                results.add(tuple(ans.copy()))
                return nums
            
            for i in range(len(nums)):
                ans.append(nums[i])
                subs(nums[i+1:],i+1,ans)
                results.add(tuple(ans.copy()))
                ans.pop()
        subs(nums1)
        results.add(tuple([]))
        return results

