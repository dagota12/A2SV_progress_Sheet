# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

import sys
from collections import defaultdict,Counter,deque
input = lambda : sys.stdin.readline().strip()
def print(*obj, sep=' ', end='\n'):
    objs = [str(i) for i in obj]
    sys.stdout.write(sep.join(objs) + end)
def lis_int():
    return [int(i) for i in input().split()]
def lis_ch():
    return [i for i in input().split()]
class UF:
    def __init__(self,n):
        n+=1
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
n,m,k = lis_int()
for _ in range(m):
    lis_int()
uf = UF(n)
q = []
for _ in range(k):
    q.append(lis_ch())
res = []
for inst, u, v in q[::-1]:
    if inst == "ask":
        if uf.find(int(u)) == uf.find(int(v)):
            res.append("YES")
        else:
            res.append("NO")
    else:
        uf.union(int(u), int(v))
print(*res[::-1],sep='\n')

