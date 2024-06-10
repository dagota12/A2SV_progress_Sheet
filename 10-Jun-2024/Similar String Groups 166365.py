# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UF:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = [0]*n
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
    def numSimilarGroups(self, strs: List[str]) -> int:
    
        """
            uf = UF(n)
            for each word in list:
                for evrey other word:
                    if current word diff with this word is 2:
                        union current group with the other
            count the group and return it
                
        """
        def diff(s1,s2):
            ct = 0
            for ch1,ch2 in zip(s1,s2):
                if ch1 != ch2:
                    ct += 1
            return ct
        n = len(strs)
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if i != j and diff(strs[i],strs[j]) <= 2:
                    uf.union(i,j)
        pars = set()
        for i in range(n):
            pars.add(uf.find(i))
        return len(pars)

        return 3