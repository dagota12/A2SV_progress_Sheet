# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs ={
        1: [(0,-1),(0,1)],2: [(-1,0),(1,0)],
        3: [(0,-1),(1,0)],4: [(0,1),(1,0)],
        5: [(0,-1),(-1,0)],6: [(0,1),(-1,0)]
        }
        valid = {
        (0, 1):{1, 3, 5},
        (0, -1):{1, 4, 6},
        (1, 0):{2, 5, 6},
        (-1, 0):{2, 3, 4}
        }
        n,m = len(grid),len(grid[0])
        visited = set()
        in_bound = lambda row,col: 0 <= row < n and 0 <= col < m
        def dfs(i,j):
            if i == n-1 and j ==m-1:
                return True
            visited.add((i,j))
            for x,y in dirs[grid[i][j]]:
                new_r,new_c = i + x,j+y
                if in_bound(new_r,new_c) and (new_r,new_c) not in visited and grid[new_r][new_c] in valid[(x,y)]:
                    if dfs(new_r,new_c):
                        return True
            return False
        return dfs(0,0)