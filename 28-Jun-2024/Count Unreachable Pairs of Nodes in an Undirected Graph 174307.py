# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UF:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = [1]*n
    def find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,x,y):
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x == par_y:
            return
        if self.size[par_x] > self.size[par_y]:
            self.parent[par_y] = par_x
            self.size[par_x] += self.size[par_y]
        else:
            self.parent[par_x] = par_y
            self.size[par_y] += self.size[par_x]

    def conn(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u,v in edges:
            uf.union(u,v)
        parents = set()
        for x in range(n):
            parents.add(uf.find(x))
        parents = list(parents)
        tot = 0
        # 3*1 + 3*2 + .. 3*t = 3*(1 + 2 + ... + t)
        for i in range(len(parents)):
            t =  n - uf.size[parents[i]]
            tot += uf.size[parents[i]] * t
            n -= uf.size[parents[i]]
        return tot