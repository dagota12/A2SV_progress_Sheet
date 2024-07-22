# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m  =  len(matrix),len(matrix[0])
        memo = {}
        def dp(i,j):
            if i < 0 or j < 0 or j >= m or i >= n:
                if i==n:
                    return 0
                return float('inf')
            if (i,j) not in memo:
                ll = dp(i+1,j-1) # bottom-left
                lb = dp(i+1,j) # bottom
                lr = dp(i+1,j+1) # bottom-right
                memo[(i,j)] = min(ll,lb,lr) + matrix[i][j]
            return memo[(i,j)]
        mi = float('inf')
        for i in range(m):
            mi = min(mi,dp(0,i))
        return mi
