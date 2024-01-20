class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        if n > len(s):
            return []
        curr_freq = defaultdict(int)
        p_freq = Counter(p)
        for i in range(n):
            curr_freq[s[i]] += 1
        l = 0
        res = []

        if curr_freq == p_freq:
            res.append(l)
            
        for r in range(n,len(s)):
            curr_freq[s[l]] -= 1
            if curr_freq[s[l]] == 0:
                curr_freq.pop(s[l])
            l+=1
            curr_freq[s[r]] += 1
            if curr_freq == p_freq:
                res.append(l)
        return res
