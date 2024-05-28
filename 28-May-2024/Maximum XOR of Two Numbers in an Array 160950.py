# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

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

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bit_len = (max(nums)).bit_length()
        trie = Trie(bit_len)
        for num in nums:
            trie.insert(num,bit_len)

        mx = 0
        for num in nums:
            mx = max(mx,trie.search(num))
        return mx