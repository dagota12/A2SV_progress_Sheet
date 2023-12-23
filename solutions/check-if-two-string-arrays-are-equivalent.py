class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 =""
        s2= ""
        for ch in word1:
            s1+= ch
        for ch in word2:
            s2+= ch
        return s1==s2