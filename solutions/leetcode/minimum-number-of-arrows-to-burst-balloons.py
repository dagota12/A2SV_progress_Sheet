class Solution(object):
    def findMinArrowShots(self, segments):
        segments.sort(key=lambda x: x[1])
        arrows, next_aim = 0, 0 #next aiming point
        for [start, end] in segments:
            if arrows == 0 or start > next_aim:
                arrows += 1
                next_aim = end
        return arrows