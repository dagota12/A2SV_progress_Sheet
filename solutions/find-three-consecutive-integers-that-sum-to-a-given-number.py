class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        m= None
        if num%3 == 0:
            m= num//3 - 1
            return [m,m+1,m+2]
        else:
            return []

