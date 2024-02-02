class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count('0')
        swaps = 0
        for ch in s:
            if ch == '0':
                zeros -= 1
            else:
                swaps += zeros
        return swaps
        