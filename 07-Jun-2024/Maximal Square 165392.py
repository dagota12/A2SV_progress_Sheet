# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        side = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    side = max(side,dp[i][j])
        return side**2
