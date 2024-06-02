# Problem: E - Reachable Arrays - https://codeforces.com/gym/524965/problem/E

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
MOD = 998244353
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    next_min = [0] * n
    dp_sum = [0] * (n + 2)
    dp_next = [0] * n

    stack_min = []
    next_min[n - 1] = n
    dp_sum[n] = 1

    for pos in range(n - 1, -1, -1):
        while stack_min and nums[stack_min[-1]] > nums[pos]:
            stack_min.pop()
        next_min[pos] = n if not stack_min else stack_min[-1]
        stack_min.append(pos)

        nxt_pos = next_min[pos]
        dp_pos = (dp_sum[pos + 1] - dp_sum[nxt_pos + 1]) % MOD
        if nxt_pos != n:
            dp_pos = (dp_pos + dp_next[nxt_pos]) % MOD
            dp_next[pos] = (dp_sum[nxt_pos] - dp_sum[nxt_pos + 1] + dp_next[nxt_pos]) % MOD

        dp_sum[pos] = (dp_pos + dp_sum[pos + 1]) % MOD

    res = 0
    min_ = nums[0]
    for i in range(n):
        min_ = min(min_, nums[i])
        if nums[i] == min_:
            res = (res + dp_sum[i] - dp_sum[i + 1]) % MOD
    print(res)
