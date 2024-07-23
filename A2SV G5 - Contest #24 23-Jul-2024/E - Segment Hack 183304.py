# Problem: E - Segment Hack - https://codeforces.com/gym/534160/problem/E

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

q = int(input())

sgt_count = defaultdict(int)
mxheap = []
mnheap = []

for _ in range(q):
    operation, l, r = input().split()
    l, r = int(l), int(r)

    if operation == '+':
        heappush(mxheap, (-l, r))
        heappush(mnheap, (r, l))
        sgt_count[(l, r)] += 1
    else:
        sgt_count[(l, r)] -= 1

    while mxheap:
            neg_left, right = mxheap[0]
            if sgt_count[(-neg_left, right)]:
                break

            else:
                heappop(mxheap)
    while mnheap:
        right, left = mnheap[0]
        if sgt_count[(left, right)]:
            break

        else:
            heappop(mnheap)

    if mxheap and mnheap and -mxheap[0][0] > mnheap[0][0]:
        print('YES')
    else:
        print('NO')