# Problem: E - Finding a Path - https://codeforces.com/gym/530187/problem/E

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

def solve():

    n, a, b = lis_int()
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v, w = lis_int()
        graph[u].append((v, w))
        graph[v].append((u, w))

    pref1 = [-1] * (n + 1)
    pref1[a] = 0
    stack = [(a, -1)]
    
    while stack:
        node, par = stack.pop()

        for ne, w in graph[node]:
            if ne != par:
                if ne == b:
                    if w ^ pref1[node] == 0:
                        return "YES"
                    continue
                
                pref1[ne] = w ^ pref1[node]
                stack.append((ne, node))
                
    ss = set(pref1)
    pref2 = [-1] * (n + 1)
    pref2[b] = 0
    stack = [(b, -1)]
    
    while stack:

        node, par = stack.pop()

        for ne, w in graph[node]:

            if ne != par:

                pref2[ne] = w ^ pref2[node]

                if pref2[ne] in ss:
                    return "YES"
                
                stack.append((ne, node))
  
    return "NO"

t = int(input())
for _ in range(t):
    print(solve())