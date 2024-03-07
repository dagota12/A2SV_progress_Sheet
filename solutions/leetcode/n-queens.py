class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag1 = set()
        diag2 = set()
        results = []
        board = [['.']*n for i in range(n)]
        def solve(r=0):
            if r >= n:
                results.append([''.join(row) for row in board.copy()])
                return
            for c in range(n):
                if c  not in col and r+c not in diag1 and c-r not in diag2:
                    board[r][c] = 'Q'
                    col.add(c)
                    diag1.add(r+c)
                    diag2.add(c-r)
                    
                    solve(r+1)

                    board[r][c] = '.'
                    col.remove(c)
                    diag1.remove(r+c)
                    diag2.remove(c-r)
        solve()
        return results

