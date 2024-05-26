# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False
def ch_idx(ch):
    return ord(ch) - ord('a')
def idx_ch(idx):
    return chr(ord('a') + idx)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for ch in word:
            idx = ch_idx(ch)
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        def dfs(node):
            if not node:
                return []
            mx_len = 0
            res = ""
            for i,child in enumerate(node.children):
                if child and child.is_end:
                    potential_ans = idx_ch(i) + (dfs(child))
                    if len(potential_ans) > len(res):
                        res = potential_ans
                    elif len(potential_ans) == len(res):
                        res = min(res,potential_ans)
            return res
        return dfs(trie.root)