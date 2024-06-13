# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for i in range(n)]
        for i in range(2, n):
            for left in range(0, n - i):
                right = left + i
                dp[left][right] = float("inf")
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + values[left]*values[right]*values[k])
        return dp[0][-1]