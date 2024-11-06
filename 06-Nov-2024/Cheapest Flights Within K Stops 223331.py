# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    heap = [(0, src, k + 1)]  # (d, u, stops)
    dist = [[math.inf] * (k + 2) for _ in range(n)]
    for u, v, w in flights:
      graph[u].append((v, w))

    while heap:
      d, u, stops = heapq.heappop(heap)
      if u == dst:
        return d
      if stops > 0:
        for v, w in graph[u]:
          newDist = d + w
          if newDist < dist[v][stops - 1]:
            dist[v][stops - 1] = newDist
            heapq.heappush(heap, (newDist, v, stops - 1))

    return -1