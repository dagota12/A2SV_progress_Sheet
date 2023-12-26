class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        for i,e in enumerate(boxes):
            if e == "1":
                ones.append(i)
        res = []
        for i in range(len(boxes)):
            tot = 0
            for c in ones:
                tot += abs(i - c)
            res.append(tot)
        return res

