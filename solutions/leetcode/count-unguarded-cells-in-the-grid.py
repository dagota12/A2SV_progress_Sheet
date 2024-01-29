class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def check(guard,grid,m,n):
            row,col = guard
            # see right
            c = col + 1
            
            while c < n and grid[row][c] != -1:
                grid[row][c] = 0
                c += 1
            # see left
            c = col - 1
            while c > -1 and grid[row][c] != -1:
                grid[row][c] = 0
                c -= 1
            # see down
            r = row + 1
            while r < m and grid[r][col] != -1:
                grid[r][col] = 0
                r += 1
            # see up
            r = row - 1
            while r > -1 and grid[r][col] != -1:
                grid[r][col] = 0
                r -= 1

        grid = []
        guards_s = frozenset([(i,j) for i,j in guards])
        walls_s = frozenset([(i,j) for i,j in walls])
        # construct the grid
        for i in range(m):
            col = []
            for j in range(n):
                if (i,j) in guards_s or (i,j) in walls_s:
                    col.append(-1)
                else:
                    col.append(1)
            grid.append(col)
        
        # for each guard check how far he can see
        for guard in guards:
            check(guard,grid,m,n)
        # count 
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count+=1
        return count

        


