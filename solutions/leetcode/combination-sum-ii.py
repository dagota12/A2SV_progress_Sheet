class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()
        candidates.sort()
        def  combine(start=0, ans =[]):
            if sum(ans) == target:
                results.add(tuple(ans))
                return 
            elif sum(ans) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                ans.append(candidates[i])
                combine(i+1,ans)
                ans.pop()
                
        combine()
        return (results)