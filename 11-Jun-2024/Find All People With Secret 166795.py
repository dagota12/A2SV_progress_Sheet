# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UF:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
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
    def reset(self,x):
        self.parent[x] = x
        self.size[x] = 1
    def conn(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        uf = UF(n)
        uf.union(0,firstPerson)# tell firt person the secreat
        i = 0
        hm = defaultdict(list)
        for meeting in meetings:
            hm[meeting[-1]].append(meeting)
        for time,sub_meetings in sorted(hm.items()):
            
            for u,v,t in sub_meetings:
                uf.union(u,v)
            for u,v,t in sub_meetings:
                if not uf.conn(u, 0):#if one of them dont know the secreate
                        uf.reset(u)
                        uf.reset(v)

        res = []
        pars = {}
        for i in range(n):
            pars[i] = uf.find(i)
            if uf.find(0) == uf.find(i):
                res.append(i)
        print(pars)
        return res
