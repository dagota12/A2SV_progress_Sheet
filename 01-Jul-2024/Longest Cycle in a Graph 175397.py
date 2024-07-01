# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        n = len(edges)
        for u,v in enumerate(edges):
            if v == -1:
                graph[u] = []
                continue
            graph[u].append(v)
        color = [0]*n
        dist,mx = defaultdict(int),-1

        def dfs(node,dis=0):
            # print(node)
            nonlocal mx
            # if node already visited on current dfs
            if color[node] == 1:
                # print(node,dis,dist)
                # print(color)
                mx = max(mx,dis - dist[node])
                return
            color[node] = 1 #visit current node
            if not (node in dist): 
                dist[node] = dis
            for neg in graph[node]:
                if color[neg] == 2:
                    continue
                dfs(neg,dis+1)
            color[node] = 2

        
        for node in range(n):
            # print(color)
            dist = defaultdict(int)
            if color[node] == 0:
                dfs(node)
        return mx