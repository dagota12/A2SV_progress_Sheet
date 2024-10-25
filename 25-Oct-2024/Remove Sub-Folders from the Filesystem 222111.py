# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for ch in word.split('/'):
            if not ch in curr.children:
                curr.children[ch] = TrieNode()
            if curr.is_end:
                return False
            curr = curr.children[ch]
        curr.is_end = True
        return True
            
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        res = []
        for f in folder:
            if trie.insert(f):
                res.append(f)
        return res


                