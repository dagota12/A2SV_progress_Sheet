class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, row_max = len(grid), {}
        col_max,total = {},0
        for i in range(n):
            row,col = grid[i][0], grid[0][i]
            for j in range(n):
                if grid[i][j]  > row:
                    row = grid[i][j]
                if grid[j][i] > col:
                    col = grid[j][i]
            row_max[i] = row
            col_max[i] = col

        for i in range(n):
            for j in range(n):
                target = min(row_max[i],col_max[j])
                total += target - grid[i][j]
        
        return total