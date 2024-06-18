# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

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
    n = int(input())
    p1,p2 = 2,3*n
    ans = []
    print((1+n)//2)
    while p1 < p2:
        print(p1,p2)
        p1+=3
        p2-=3
