# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mx,n = 0,len(words)
        for i in range(n):
            words[i] = [set(words[i]),len(words[i])]
        for i in range(n):
            for j in range(i+1,n):
                if not (words[i][0] & words[j][0]):
                    mx = max(mx,words[i][1] * words[j][1])
        return mx