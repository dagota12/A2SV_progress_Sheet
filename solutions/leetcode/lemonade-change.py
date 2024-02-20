class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change ={5:0,10:0,20:0}   
        for i in range(len(bills)):
            bill = bills[i]
            if bill == 5:
                change[bill] += 1
            elif bill == 10:
                change[10] += 1
                change[5] -= 1
            elif bill == 20:
                change[20] += 1
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            for v in change.values():
                if v < 0:
                    return False
        return True