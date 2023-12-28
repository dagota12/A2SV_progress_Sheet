class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        res = 2001
        for e in fronts:
            if not e in same:
                res = min(res,e)
        for e in backs:
            if not e in same:
                res = min(res,e)
        return res if res<2001 else 0

