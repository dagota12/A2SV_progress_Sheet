class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_freq = Counter(t)
        freq = Counter()
        min_ = ""
        min_leng = len(s)
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while t_freq - freq == Counter():
                if (min_leng >= r - l + 1):
                    min_leng = r-l+1
                    min_ = s[l:r+1]
                freq[s[l]] -= 1
                l+=1
            
        return min_
                     
