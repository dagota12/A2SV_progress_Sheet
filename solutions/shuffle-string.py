class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res =[0]*len(s)
        for idx,e in enumerate(indices):
             res[e] = s[idx]
        return "".join(res)