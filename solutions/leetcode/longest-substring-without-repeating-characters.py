class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        hash_map = defaultdict(int)# tracks count of current window elements
        for r in range(len(s)):
            hash_map[s[r]] += 1
             # if we found duplicate remove it until we don't have duplicate
            while hash_map[s[r]] > 1:
                hash_map[s[l]] -= 1
                l += 1
            max_len = max(max_len,r - l + 1)
        return max_len
            