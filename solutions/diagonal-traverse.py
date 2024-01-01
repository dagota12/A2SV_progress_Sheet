class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diags[i+j].append(mat[i][j])
        res = []
        for k,v in diags.items():
            if k % 2 == 1:
                res.extend((diags[k]))
            else:
                res.extend(reversed(diags[k]))
        return res
