# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

import sys
from heapq import *
from collections import defaultdict,Counter,deque
input = lambda : sys.stdin.readline().strip()
def print(*obj, sep=' ', end='\n'):
    objs = [str(i) for i in obj]
    sys.stdout.write(sep.join(objs) + end)
def lis_int():
    return [int(i) for i in input().split()]
def lis_ch():
    return [i for i in input().split()]
def dp(i,health):
    if health < 0:
        return float('-inf')
    if i >= n:
        if health >= 0:
            return 0
        return float('-inf')
    if (i,health) not in memo:
        drink = dp(i+1,health+ nums[i]) + 1
        dont = dp(i+1,health)
        memo[(i,health)] = max(drink,dont)
    return memo[(i,health)]

import sys, threading
def main():
    n = int(input())
    nums = lis_int()
    ct,heap = 0,[]
    health = 0
    for i in range(n):
        # print(health,nums[i],heap)
        if nums[i] >= 0:
            health += nums[i]
            ct += 1
        elif health + nums[i] >= 0:
            heappush(heap,nums[i])
            health += nums[i]
            ct += 1
        else:
            if heap:
                if heap[0] < nums[i]:
                    ele = heappop(heap)
                    # print(ele)
                    health += nums[i]-ele
                    heappush(heap,nums[i])

    print(ct)

main()
