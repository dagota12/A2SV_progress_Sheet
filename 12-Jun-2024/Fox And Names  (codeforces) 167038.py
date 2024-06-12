# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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
def idx_ch(idx):
    return chr(ord('a') + idx)
def ch_idx(ch):
    return ord(ch) - ord('a')
n = int(input())
graph = defaultdict(list)
names = []
deg = [0]*26
for _ in range(n):
    name = input()
    if not names:
        names.append(name)
        continue
    p1,p2 = 0,0
    mi = min(len(name),len(names[-1]))
    for i in range(mi):
        if name[i] != names[-1][i]:
            graph[names[-1][i]].append(name[i])
            deg[ch_idx(name[i])] += 1
            break
    else:
        if len(name) < len(names[-1]):
                print("Impossible")
                exit(0)
    names.append(name)

# print(graph)
import sys, threading
colors = [0]*26
res = []
def dfs(node):
    # print(node)
    if colors[node] == 1:
        return False
    colors[node] = 1
    valid = True
    for neg in graph[idx_ch(node)]:
        if colors[ch_idx(neg)] == 2:
            continue
        valid = valid and dfs(ch_idx(neg))
    colors[node] = 2
    res.append(idx_ch(node))
    return valid
    
def main():
    for ch in 'acbdefhijklmnogpqrstuvwxyz':
        if colors[ch_idx(ch)] == 0:
            if not dfs(ch_idx(ch)):
                print("Impossible")
                exit(0)
    # print(colors)
    print(''.join(res)[::-1])

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()