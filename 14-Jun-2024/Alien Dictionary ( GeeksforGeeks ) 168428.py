# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from collections import *
def ch_idx(ch):
    return ord(ch) - ord('a')
def idx_ch(idx):
    return chr(ord('a') + idx)  
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        n = len(alien_dict)
        if N < 2:
            return alien_dict[0][0]
        deg = {idx_ch(i):0 for i in range(K)}
        for i in range(n-1):
            ln = min(len(alien_dict[i]),len(alien_dict[i+1]))
            for j in range(ln):
                if alien_dict[i][j] != alien_dict[i+1][j]:
                    graph[alien_dict[i][j]].append(alien_dict[i+1][j])
                    idx = (alien_dict[i+1][j])
                    idx2 = (alien_dict[i][j])
                    if idx2 not in deg:
                        deg[idx2] = 0
                    deg[idx] += 1
                    break
        res = []
        # print(deg)
        queue = deque([ch for ch in deg if deg[ch] == 0])
        while queue:
            node = queue.popleft()
            res.append((node))
            for neg in graph[node]:
                deg[(neg)] -= 1
                if deg[(neg)] == 0:
                    queue.append(neg)
        
        return res