class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board),len(board[0])
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        def dfs(r,c,idx):
            nonlocal n,m,visited
            if idx >= len(word):
                return True
            in_bound = lambda x,y: x < n and x > -1 and y < m and y > -1
            visited.add((r,c))
            for x,y in dir:
                seen = (r + x,c + y) in visited
                if in_bound(r + x, c + y) and (not seen) and board[r+x][c+y] == word[idx]:
                    if(dfs(r + x,c + y, idx+1)):
                        return True
            visited.remove((r,c))
            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i,j,1):
                        return True
        return False