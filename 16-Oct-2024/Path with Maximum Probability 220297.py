# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[u].append([v,succProb[i]])
            graph[v].append([u,succProb[i]])
        # print(graph)
        queue = [(-1,start)]# queue :[prob,node]
        visited = set([start])
        while queue:
            prob,node = heappop(queue)
            visited.add(node)
            if node == end:
                return prob * -1
            for neg,p in graph[node]:
                if not neg in visited:
                    heappush(queue,[prob*p,neg])

        return 0

