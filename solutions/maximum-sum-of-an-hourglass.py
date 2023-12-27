class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def hourSum(i,j,row,col,grid):
            if i + 2 >= row or j + 2 >= col:
                return -1
            sum1 = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
            return sum1
        
        mx = -1

        for i in range(row):
            for j in range(col):
                mx = max(mx,hourSum(i,j,row,col,grid))
        return mx
