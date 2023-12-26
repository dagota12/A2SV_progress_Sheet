class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        p = 0
        res = []
        for i in range(len(s)):
            if p < len(spaces) and i == spaces[p]:
                res.append(" ")
                p+=1
            res.append(s[i])
        return "".join(res)


            
