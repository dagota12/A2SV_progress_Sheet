class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        
        if len(mat) == 1:
            return mat[0][0]
        
        for i in range(len(mat)):
            diag_sum += mat[i][i]
            
            if i == len(mat)//2 and len(mat) % 2:
                continue
            
            diag_sum += mat[(len(mat) - 1) - i][i]
        
        return diag_sum