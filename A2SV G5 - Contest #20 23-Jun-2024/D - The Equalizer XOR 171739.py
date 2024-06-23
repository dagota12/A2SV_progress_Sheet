# Problem: D - The Equalizer XOR - https://codeforces.com/gym/528792/problem/D

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
    nums = lis_int()
    xor = [nums[0]]
    for i in range(1,n):
        xor.append(xor[i-1] ^ nums[i])
    ans = "NO"
    if xor[-1] == 0:
        print("YES")
        continue
    ans = "NO"
    for i in range(n):
        first = xor[i]
        for j in range(i+1,n):
            second = xor[j] ^ xor[i]
            third = xor[-1] ^ xor[j]
            if first == second == third:
                ans = "YES"
                break
    print(ans)

       