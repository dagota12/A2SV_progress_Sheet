class Solution:
    def totalMoney(self, n: int) -> int:
        tot = 0
        inc = 1
        pm = 1
        i = 1
        while i <= n:
            tot += inc
            if i%7 == 0:
                pm+=1
                inc = pm-1
            inc+=1
            i+=1
        return tot
            