class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid//m][mid % m] == target:
                return True
            elif matrix[mid//m][mid % m] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
