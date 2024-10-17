# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start,end in intervals:
            events.append([start,1])
            events.append([end+1,-1])
        events.sort()
        # calculate maximun number of intersections at the same time
        mi = 0
        running_sum = 0
        for _,x in events:
            running_sum += x
            mi = max(mi,running_sum)
        return mi
