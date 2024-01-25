class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix) ,len(matrix[0]) 
        self.matrix = [[0]*(m + 1) for i in range(n + 1)] # generate an offsetted matrix(0 filled) by 1
        #pre-compute the prefix sum
        for r in range(1,n+1):
            for c in range(1,m+1):
                prev_sums = self.matrix[r-1][c] + self.matrix[r][c-1] - self.matrix[r-1][c-1]
                self.matrix[r][c] = matrix[r-1][c-1] + prev_sums


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #
        top = self.matrix[row1][col2+1]
        left = self.matrix[row2+1][col1]
        big_sum = self.matrix[row2+1][col2+1]
         
        return big_sum - top - left + self.matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)