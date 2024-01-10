class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        p1 = 0
        p2 = 0
        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 > 0 and typed[p2] == typed[p2 - 1]:
                p2 += 1
            else:
                return False
        if p1 != len(name):
            return False
        for i in range(p2, len(typed)):
            if typed[i] != name[-1]:
                return False
        return True