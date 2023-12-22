class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        res = ""
        mx = 0
        for word in words:
            if len(word) > mx:
                mx = len(word)
        res=[]
        for j in range(mx):
            col = ""
            for i in range(len(words)):
                if j < len(words[i]):
                    col +=words[i][j] 
                else: col+=" "
            res.append(col.rstrip())
        return res
