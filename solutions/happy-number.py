class Solution:
    def isHappy(self, n: int) -> bool:
        prevs = set()
        while(n!=1):
            x = str(n)
            happy_sum = 0
            for e in x:
                happy_sum += int(e)**2
            if happy_sum == 1:
                return True
            if happy_sum in prevs:
                return False
            prevs.add(happy_sum)
            n = happy_sum
        return True

