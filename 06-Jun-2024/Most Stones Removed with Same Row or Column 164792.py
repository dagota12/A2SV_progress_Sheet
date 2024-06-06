# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

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
    def __str__(self):
        return str(self.parent)
    def conn(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n =len(stones)
        uf = UF(n)
        stones = [(val,i) for i,val in enumerate(stones)]
        stones.sort(key =lambda x:x[0])
        for i in range(n-1):
            pos,idx = stones[i]
            n_pos,n_idx = stones[i+1]
            if pos[0] == n_pos[0]:
                uf.union(idx,n_idx)
        stones.sort(key =lambda x:x[0][-1])
        # print(stones)
        for i in range(n-1):
            pos,idx = stones[i]
            n_pos,n_idx = stones[i+1]
            if pos[1] == n_pos[1]:
                uf.union(idx,n_idx)
        parents = set()
        for x in range(n):
            parents.add(uf.find(x))
        removed = 0

        for p in parents:
            removed += uf.size[p] - 1
        return removed