# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        incedence  = defaultdict(int)
        for u,v in edges:
            incedence[u] += 1
            incedence[v] += 1
        for k,v in incedence.items():
            if v == len(edges):
                return k