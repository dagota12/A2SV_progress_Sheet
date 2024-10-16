# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowles = set("aeiou")
        count = 0
        for i in range(n):
            if word[i] in vowles:
                count += (i+1) * (n - i)
        return count

"""
aaa
word = "aba"
conut = [1,0,1]
prefix sum = [1,1,2]

"""