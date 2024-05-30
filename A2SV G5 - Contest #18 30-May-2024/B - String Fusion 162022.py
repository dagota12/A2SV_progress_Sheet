# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

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

def ch_idx(ch):
    return ord(ch) - ord('a')
def idx_ch(idx):
    return chr(ord('a') + idx)
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.ct = 0
        self.is_end = False
    def __str__(self):
        return self._print_trie_node()
    def _print_trie_node(self, prefix=""):
        output = ""
        if self.is_end:
            output += prefix + " | "
        for idx,child in enumerate(self.children):
            if child:
                output += child._print_trie_node(prefix + idx_ch(idx))
        return output
def ch_idx(ch):
    return ord(ch) - ord('a')
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for ch in word:
            idx = ch_idx(ch)
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur.children[idx].ct += 1
            cur = cur.children[idx]
        cur.is_end = True
    def search(self,word):
        cur = self.root
        res = 0
        for ch in word:
            idx = ch_idx(ch)
            if not cur.children[idx]:
                return res
            cur = cur.children[idx]
            res += cur.ct * 2
        return res


n = int(input())
trie = Trie()
s = [] 
for _ in range(n):
    s.append(input())
    trie.insert(s[-1])
# print(trie.root)
total = sum([len(word)*2*n for word in s])
for word in s:
	total -= trie.search(word[::-1])
print(total)