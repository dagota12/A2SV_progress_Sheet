class Solution:
    def balancedString(self, s: str) -> int:

        req_count = len(s)//4
        def balanced(freq: dict):
            for ch in freq:
                if freq[ch] > req_count:
                    return False
            return True
        
        freq = Counter(s)
        if balanced(freq):
            return 0
        curr_freq = defaultdict(int)
        res = len(s)
        l = 0
        for r in range(len(s)):
            freq[s[r]] -= 1
            while balanced(freq) and l < len(s):
                res = min(res,r - l + 1)
                freq[s[l]] += 1
                l += 1
        return res