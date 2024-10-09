# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowles = set('aeiou')
        vowles = [ord(ch) if ch in vowles else 0 for ch in s]
        for i in range(1,len(vowles)):
            vowles[i] ^= vowles[i-1]
        # how do i calculate the longest subarry with xor 0 ?
        # if we concider xor ax a bucket that removes dubbles
        #  [b,a,a] the xor is b meaning the substring from the previous occurence of
        # the value b note here we consider the first occurence 
        # because we need the longerst substring
        hm = {0:-1}
        mx = 0
        for i,val in enumerate(vowles):
            if val in hm:
                mx = max(mx,i - hm[val])
            else:
                hm[val] = i
        return mx