# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

import sys
from collections import defaultdict,Counter,deque
from math import ceil
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
    n, k, x = lis_int()
    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))
    elif k == 1 or (k == 2 and n % 2):
	    print("NO")

    else:
        print("YES")
        print(n // 2)
            
        print(*([2] * (n // 2 - 1)) + [3 if n % 2 == 1 else 2])
