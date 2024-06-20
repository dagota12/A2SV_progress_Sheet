# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

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
    n, k = map(int, input().split())
    cost = [0] + lis_int()
    nums = set(lis_int())

    graph = defaultdict(list)
    degree = [0] * (n + 1)
    future = [0] * (n + 1)
    ans = [0] * (n + 1)
    
    for i in range(1, n + 1):
        line = lis_int()
        m, edges = line[0], line[1:]
        if i in nums:
            continue
        degree[i] = m
        for a in edges:
            graph[a].append(i)

    queue = deque()
    for node in range(1, n + 1):
        if node in nums:
            queue.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            queue.append(node)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            degree[child] -= 1
            future[child] += ans[node]
            if degree[child] == 0:
                queue.append(child)
                ans[child] = min(cost[child], future[child])

    print(*ans[1:])

q = int(input())
for _ in range(q):
	solve()
