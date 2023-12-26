class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        coverd = set()
        needed = {i for i in range(left,right+1)}
        for r in ranges:
            for i in range(r[0],r[1]+1):
                coverd.add(i)
        return needed.issubset(coverd)
