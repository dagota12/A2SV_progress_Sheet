class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        most_frequent = 0
        l = 0
        max_len = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_frequent = max(most_frequent, freq[s[r]])
            
            if (r - l + 1) - most_frequent > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        
        return max_len