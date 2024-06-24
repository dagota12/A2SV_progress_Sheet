# Problem: E - Voyage Quest - https://codeforces.com/gym/528792/problem/E

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
x_1, y_1 = lis_int()
x_2, y_2 = lis_int()
n = int(input())
s = input()
find = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}
def check(k):
    x_3, y_3 = x_1, y_1
    full_cycles = k // n
    extra_days = k % n

    for ch in s:
        x_3 += find[ch][0] * full_cycles
        y_3 += find[ch][1] * full_cycles
    
    for i in range(extra_days):
        x_3 += find[s[i]][0]
        y_3 += find[s[i]][1]
        
    return abs(x_2 - x_3) + abs(y_2 - y_3) <= k

l,r = 0,10**15
while l <= r:
    mid = l + (r-l)//2
    # print(mid)
    # break

    if check(mid):
        r = mid - 1
    else:
        l = mid + 1
if l > 10**15:
    print(-1)
else:
    print(l)