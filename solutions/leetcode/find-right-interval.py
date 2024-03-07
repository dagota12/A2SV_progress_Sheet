class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i,inter in enumerate(intervals):
            inter.append(i)
        intervals.sort()
        res = [-1] * n
        
        # for each element calculate left
        for inter in intervals:
            l,r,best = 0, n - 1, -1
            
            start,end,idx = inter
            # print(end)
            while l <= r:
                mid = l + (r-l)//2
                if end <= intervals[mid][0]:
                    res[idx] = intervals[mid][-1]
                    best = mid
                if end > intervals[mid][0]:
                    l = mid + 1
                else:
                    r = mid - 1


        return res