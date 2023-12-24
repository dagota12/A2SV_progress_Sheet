class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        mv = 0
        for i in range(len(points)-1):
            xo,yo = points[i]
            x2,y2 = points[i+1]
            diag = min( abs(x2-xo), abs(y2-yo) )
            remaining = max(abs(x2-xo), abs(y2-yo)) - diag
            mv+= diag + remaining
        return mv
