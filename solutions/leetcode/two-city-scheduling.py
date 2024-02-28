class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[1] - x[0])
        tot,n = 0,len(costs)
        for i in range(n):
            if i < n//2:
                tot += costs[i][1]
            else:
                tot += costs[i][0]
        return tot
    