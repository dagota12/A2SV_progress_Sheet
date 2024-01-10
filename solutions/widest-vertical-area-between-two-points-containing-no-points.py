class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        max_ = -1

        for i in range(1,len(points)):
            p2,p1 = points[i],points[i-1]
            if p2[0] - p1[0] > max_:
                max_ = p2[0] - p1[0]
        return max_

