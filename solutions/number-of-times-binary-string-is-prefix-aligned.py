class Solution:
    def numTimesAllBlue(self, A):
        lighted_bulb, res = 0,0
        for i, a in enumerate(A):
            lighted_bulb = max(lighted_bulb, a)
            res += lighted_bulb == i + 1
        return res    