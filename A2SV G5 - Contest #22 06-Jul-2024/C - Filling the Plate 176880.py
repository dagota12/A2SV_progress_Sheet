# Problem: C - Filling the Plate - https://codeforces.com/gym/531455/problem/C

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
import sys

k,n,m = lis_int()
input() #for the empty spaces 

plate = []
for i in range(k):
    rect = []
    for j in range(n):
        elem = []
        for c in sys.stdin.readline()[:-1]:
            elem.append(c == '.')
        rect.append(elem)
    plate.append(rect)
    input() #for the empty spaces
        
info = lis_int()
waterX = int(info[0]) - 1
waterY = int(info[1]) - 1

visited = set()
stack = [(waterX, waterY, 0)]

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

time = 0
while len(stack) != 0:
    cur = stack.pop()
    
    if cur in visited:
        continue

    visited.add(cur)
    curX = cur[0]
    curY = cur[1]
    curZ = cur[2]
    time += 1

    for dd in direction:
        newX = curX + dd[0]
        newY = curY + dd[1]
        newZ = curZ + dd[2]

        if newX >= 0 and newX < n and newY >= 0 and newY < m and newZ >= 0 and newZ < k:
            if plate[newZ][newX][newY]:
                stack.append((newX, newY, newZ))

print(time)
