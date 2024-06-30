# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UF:
    
    def __init__(self, n):
        self.count = n               
        self.parent = list(range(n))
        self.rank = [1]*n           
        
    def find(self, x):
        if x != self.parent[x]: 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
    
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y: return False
        self.count -= 1 
        if self.rank[par_x] > self.rank[par_y]: par_x, par_y = par_y, par_x 
        self.parent[par_x] = par_y
        self.rank[par_y] += self.rank[par_x] 
        return True
    
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UF(n) # for Alice
        ufb = UF(n) # for Bob
        
        ans = 0
        edges.sort(reverse=True) 
        for t, u, v in edges: 
            u, v = u-1, v-1
            if t == 3: ans += not (ufa.union(u, v) and ufb.union(u, v)) # Alice & Bob
            elif t == 2: ans += not ufb.union(u, v)                     # Bob only
            else: ans += not ufa.union(u, v)                            # Alice only
        return ans if ufa.count == 1 and ufb.count == 1 else -1 # check if uf is connected 