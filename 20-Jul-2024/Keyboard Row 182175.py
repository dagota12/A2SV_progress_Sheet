# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res =[]
        rows ={ 0 : set("qwertyuiopQWERTYUIOP"), 1 : set("asdfghjklASDFGHJKL"), 2 : set("zxcvbnmZXCVBNM") }
        for word in words:
            s = set(word)
            if s.issubset(rows[0]) or s.issubset(rows[1]) or s.issubset(rows[2]):
                res.append(word)
        return res