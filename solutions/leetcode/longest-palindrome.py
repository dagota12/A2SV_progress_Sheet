class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        max_len = 0
        for ch in s:
            freq[ch] += 1
        odd = False
        for k,v in freq.items():
            if v % 2 == 0:
                max_len += v
            else:
                max_len += v - 1
                odd = True
        if odd: max_len += 1
        return max_len

