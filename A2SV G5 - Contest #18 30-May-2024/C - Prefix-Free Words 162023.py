# Problem: C - Prefix-Free Words - https://codeforces.com/gym/526229/problem/C

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
                output += child._print_trie_node(prefix + str(idx))
        return output
def ch_idx(children):
    return ord(children) - ord('a')
def idx_ch(idx):
    return chr(ord('a') + idx)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,bit):
        cur = self.root
        for children in word:
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True
    def all_end(self,node) -> bool:
        for idx,child in enumerate(node.children):
            if not child or node.children[idx].is_end == False:
                return False
        return True
    def add(self,length):
        trie,res = self.root,[]
        stack = []
        for i in range(length):
            stack.append(trie)
            if trie.children[0] is None or not trie.children[0].is_end:
                if trie.children[0] is None:
                    trie.children[0] = TrieNode()
                trie = trie.children[0]
                res.append('0')
            elif trie.children[1] is None or not trie.children[1].is_end:
                if trie.children[1] is None:
                    trie.children[1] = TrieNode()
                trie = trie.children[1]
                res.append('1')
            else:
                return False
        trie.is_end = True
        while stack and stack[-1].children[1] and stack[-1].children[1].is_end:
            prev = stack.pop()
            prev.is_end = True
        return ''.join(res)


def main():
    n = int(input())
    nums = lis_int()
    nums = [(x,i) for i,x in enumerate(nums)]
    nums.sort()
    trie = Trie()
    res = ["YES"] + [None]*n
    for num,idx in nums:
        ans = trie.add(num)
        if ans == False:
            res = ["NO"]
            break
        res[idx+1] = ''.join(ans)
    print(*res,sep='\n')
    
main()