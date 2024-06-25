# Problem: C - K-Complete Word - https://codeforces.com/gym/527294/problem/C

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
t = int(input())
for _ in range(t):
    n, k = lis_int()
    s = input()
    
    freq = defaultdict(Counter)
    for i in range(n):
        loc = min(i % k, k - i % k - 1)
        freq[loc][s[i]] += 1
    
    changes = 0
    tot = 2 * (n // k)
    for i in range(k // 2):
        max_freq= max(freq[i].values())
        changes += tot - max_freq
    
    if k % 2:
        max_freq = max(freq[k//2].values())
        changes += n//k - max_freq
    
    print(changes)


