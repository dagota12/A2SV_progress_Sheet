# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D

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
class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.is_end = False
    def __str__(self):
        return self._print_trie_node()

    def _print_trie_node(self, prefix=""):
        output = ""
        if self.is_end:
            output += prefix + " | "
        for idx,child in enumerate(self.children):
            if child:
                output += child_node._print_trie_node(prefix + str(idx))
        return output
class Trie:
    def __init__(self,bit_len):
        self.root = TrieNode()
        self.bit_len = bit_len
    def insert(self,num,bit_len):
        cur = self.root
        for shift in range(bit_len-1,-1,-1):
            bit = (num >> shift)  & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.is_end = True
    def search(self,num):
        mx = 0
        cur = self.root
        for shift in range(self.bit_len-1,-1,-1):
            bit = (num >> shift)  & 1
            if  not cur.children[1-bit]:
                cur = cur.children[bit]
            else:
                mx |= (1<<shift) 
                cur = cur.children[1 - bit]
        return mx
            
n = int(input())
nums = lis_int()
bit_len = (max(nums)).bit_length()
prefix,suffix = [0]*(n+1),[0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] ^ nums[i]
    suffix[n-1-i] = suffix[n-i] ^ nums[n-1-i]
trie = Trie(bit_len)
for num in prefix:
    trie.insert(num,bit_len)
mx = 0
for i in range(n-1,-1,-1):
    mx = max(mx,trie.search(suffix[i]))
print(mx)