class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        hm = {}
        ch = ord('a')
        res= ""
        for i in range(1,27):
            hm[str(i)] = chr(ch)
            ch+=1
    
        i=0
        while i < len(s):
            if i+3 <= len(s) and s[i+3-1] == "#":
                res+=hm[s[i:i+2]]
                i+=3
            else:
                res+=hm[s[i]]
                i+=1
        return res
