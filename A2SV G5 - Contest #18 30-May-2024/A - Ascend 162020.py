# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

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
n = int(input())
nums=lis_int()
mx = 1
l = 1
for i in range(1,n):
    if nums[i-1] >= nums[i]:
        l = 1
    else:
        l+=1
    mx = max(mx,l)
print(mx)
