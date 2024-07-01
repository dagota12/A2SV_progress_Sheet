# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        time = 1
        visited_time = [0] * len(edges)

        for i, edge in enumerate(edges):
            if visited_time[i]:
                continue
            startTime = time
            u = i
            while u != -1 and not visited_time[u]:
                visited_time[u] = time
                time += 1
                u = edges[u]
            if u != -1 and visited_time[u] >= startTime:
                ans = max(ans, time - visited_time[u])

        return ans
