# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

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
    def __init__(self,n,nums):
        n+=1
        self.parent = {i:i for i in range(n)}
        self.size = [0]*n
        self.tot = nums
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
            self.tot[par_x] += self.tot[par_y]
        else:
            self.parent[par_x] = par_y
            self.size[par_y] += self.size[par_x]
            self.tot[par_y] += self.tot[par_x]
    def conn(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UF(n,nums)
        arr,ans = [-1]*n,[]
        mx = 0
        
        for idx in removeQueries[::-1]:
            ans.append(mx)
            if idx + 1 < n and arr[idx+1] != -1:
                uf.union(idx,idx+1)
            if idx - 1 >= 0 and arr[idx-1] != -1:
                uf.union(idx,idx-1)
            arr[idx] = 1
            mx = max(mx,uf.tot[uf.find(idx)])
        return ans[::-1]
        


