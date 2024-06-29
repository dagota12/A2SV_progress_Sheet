# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        diff_prof,n  = list(zip(difficulty,profit)),len(worker)
        diff_prof.sort()
        # print(diff_prof)
        heap,p,tot = [],0,0
        for i in range(n):
            while p < len(profit) and diff_prof[p][0] <= worker[i]:
                heappush(heap,-diff_prof[p][1])
                p += 1
            if heap:
                tot += -heap[0]
        return tot
        