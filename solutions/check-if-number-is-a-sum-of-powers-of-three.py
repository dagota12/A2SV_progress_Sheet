class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if not (n%3 == 1 or n%3 == 0):
                return False
            n//= 3
        return True
            


