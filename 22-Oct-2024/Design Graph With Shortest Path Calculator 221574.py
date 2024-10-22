# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u,v,w in edges:
            self.graph[u].append([v,w])

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.graph[u].append([v,w])

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")]*self.n
        dist[node1] = 0
        queue = [(0,node1)] #priority queue (dist,node)
        visited = set()
        while queue:
            d,node = heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            for neg,w in self.graph[node]:
                new_dist = d + w
                if new_dist < dist[neg]:
                    dist[neg] = new_dist
                    heappush(queue,[new_dist,neg])
        res = dist[node2]
        return res if res != float("inf") else -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)