# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        in_bound = lambda r,c: 0<=r<n and 0<=c<m
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*m for _ in range(n)]

        def dfs(row,col):
            # print(row,col,"-",grid[row][col])

            visited[row][col] = True
            fishes = grid[row][col]
            for x,y in dirs:
                new_r,new_c = row+x,col+y
                # print(in_bound(new_r,new_c))
                if in_bound(new_r,new_c) and grid[new_r][new_c] != 0 and not visited[new_r][new_c]:
                    ans = dfs(new_r,new_c)
                    fishes += ans
                    # print(fishes)
            
            return fishes
        mx_fishes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not visited[i][j]:
                    mx_fishes = max(mx_fishes,dfs(i,j))
                    
        return mx_fishes