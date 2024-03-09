class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def combine(k,start= 1,ans=[]):
            if k == 0:
                if sum(ans) == n:
                    res.append(ans.copy())
                return
            for i in range(start,10):
                ans.append(i)
                combine(k-1,i+1)
                ans.pop()
        combine(k)
        return res
