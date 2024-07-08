# Problem: D - Counting Hack - https://codeforces.com/gym/534160/problem/D

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
for _ in range(int(input())):
    n = int(input())
    arr = lis_int()

    visited = set()
    right_most = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if arr[i] not in visited:
            visited.add(arr[i])
            right_most[i + 1] = 1
            visited.add(arr[i])
    
    for i in range(1, len(right_most)):
        right_most[i] += right_most[i - 1]

    visited.clear()
    ans = 0
    for i in range(n):
        if arr[i] not in visited:
            ans += right_most[-1] - right_most[i]
            visited.add(arr[i])

    print(ans)