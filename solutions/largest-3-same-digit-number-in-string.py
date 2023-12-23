class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = []
        c = 1
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                c+=1
            else:
                c=1
            if c == 3:
                good.append(str(num[i] * 3))
        good.sort()
        return good[-1] if good else ""


            
