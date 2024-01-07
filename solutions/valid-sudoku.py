class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board),len(board[0])
        rowSet = set()
        colSet = set()
        boxSet = set()
        
        for i in range(n):
            for j in range(m):
                boxElem = board[3*(i//3) + j//3][( (i*3) % 9) + j%3]
                if board[i][j] != "." and board[i][j] in rowSet:
                    return False
                elif board[j][i] != "." and board[j][i] in colSet:
                    return False
                elif boxElem != "." and boxElem in boxSet:
                    return False
                rowSet.add(board[i][j])
                colSet.add(board[j][i])
                boxSet.add(boxElem)
            rowSet.clear()
            colSet.clear()
            boxSet.clear()
            
        return True