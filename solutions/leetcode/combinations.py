class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combine(n,k,start=1,ans = []):
            if k == 0:
                res.append(ans.copy())
                return
            for i in range(start,n+1):
                ans.append(i)
                combine(n,k - 1,i+1,ans)
                ans.pop()
        combine(n,k)
        return res