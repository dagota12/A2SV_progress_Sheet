class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(r):
            if r == 0:
                return [1]

            prev_row = pascal(r-1)
            new_row = [1]
            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i]+prev_row[i+1])
            new_row.append(1)

            return new_row
        return pascal(rowIndex)
