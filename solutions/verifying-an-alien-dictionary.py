class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        refer ={}
        for i,o in enumerate(order):
            refer[o] = i
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            j=0
            while j < len(word1) and j < len(word2):
                if refer[word1[j]] > refer[word2[j]]:
                    return False
                elif refer[word1[j]] < refer[word2[j]]:
                    j+=1
                    break
                j+=1
            
            if len(word1) > len(word2) and word1[:j] == word2[:j]:
                return False
            
        return True