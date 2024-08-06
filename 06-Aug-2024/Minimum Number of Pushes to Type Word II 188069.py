# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0]*26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        freq.sort(reverse=True)
        res = 0
        for i,nm in enumerate(freq):
            res += nm * (1 + i//8)
        return res