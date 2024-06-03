# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

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
        self.size = [1]*n
        self.min = {i:i for i in range(n)}
        self.max = {i:i for i in range(n)}
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

            self.min[par_x] = min(self.min[par_x],self.min[par_y])
            self.max[par_x] = max(self.max[par_x],self.max[par_y])
            
        else:
            self.parent[par_x] = par_y
            self.size[par_y] += self.size[par_x]
            self.min[par_y] = min(self.min[par_x],self.min[par_y])
            self.max[par_y] = max(self.max[par_x],self.max[par_y])
    def conn(self,x,y):
        return self.find(x) == self.find(y)
n,q = lis_int()
uf = UF(n)
for _ in range(q):
    cmd = input()
    if cmd[0] == 'u':
        x,y = list(map(int,cmd.split()[1:]))
        uf.union(x,y)
        # print(uf.size)
    else:
        x = list(map(int,cmd.split()[1:]))[0]
        # print(uf.parent[x])
        size = uf.size[uf.find(x)]
        mi = uf.min[uf.find(x)]
        mx = uf.max[uf.find(x)]
        print(mi,mx,size)