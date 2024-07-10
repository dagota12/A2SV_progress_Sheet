# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = []
        for word in strs:
            words.append((sorted(word),word))
        words.sort()
        words.append(("*","*"))
        res = []
        prev,group = None, []
        for key,word in words:
            if prev == None or key == prev:
                group.append(word)
            else:
                res.append(group.copy())
                group = [word]
            
            prev = key
        # print(res)
        return res
