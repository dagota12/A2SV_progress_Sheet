class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        def  combine(start=0, ans =[]):
            if sum(ans) == target:
                results.add(tuple(ans))
                return 
            elif sum(ans) > target:
                return
            for i in range(start, len(candidates)):
                ans.append(candidates[i])
                combine(i+1,ans)
                combine(i,ans)
                ans.pop()
        combine()
        return (results)

