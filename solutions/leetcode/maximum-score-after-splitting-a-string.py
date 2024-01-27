class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == '0' else 0
        right = s[1:].count('1')
        score = left + right
        for ch in s[1:-1]:
            if ch == '1':
                right -= 1
            else:
                left += 1
            score = max(score,left+right)
        return score

