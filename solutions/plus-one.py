class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for x in digits:
            n = n*10 + x
        res = []
        n = str(n+1)
        for x in n:
            res.append(int(x))
        return res
