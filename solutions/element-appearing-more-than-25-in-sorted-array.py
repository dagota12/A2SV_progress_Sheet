class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        g = len(arr) * 0.25
        freq = {}
        for e in arr:
            freq[e] = freq.get(e,0) + 1
            if freq[e] > g:
                return e
        return 1