class Solution:
    def valid(self,board,r,c,val):
        n = len(board)

        for j in range(n): # validate row
            if str(val) == board[r][j]:
                return False
        for j in range(n): # validate col
            if str(val) == board[j][c]:
                return False
        row = 3 * (r//3)
        col = 3 * (c//3)
        for i in range(row,row + 3):
            for j in range(col,col + 3):
                if str(val) == board[i][j]:
                    return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        def solve(r,c):
            if r == n:
                return True
            if c == n:
                return solve(r+1,0)
            if board[r][c] == '.':
                for num in range(1,10):
                    if self.valid(board,r,c,num):
                        board[r][c] = str(num)
                        # print(f"Placed {num} at position ({r}, {c})")
                        if solve(r,c+1):
                            return True
                        board[r][c] = "."
                        # print(f"Backtracked at position ({r}, {c})")
                return False
            else:
                return solve(r,c+1)

        solve(0,0)

        """
        Do not return anything, modify board in-place instead.
        """
        