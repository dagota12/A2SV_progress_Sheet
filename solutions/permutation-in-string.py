class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        
        for char in s1:
            s1_freq[char] += 1
        
        for i in range(len(s1)):
            s2_freq[s2[i]] += 1
        
        if s1_freq == s2_freq:
            return True
        
        for i in range(len(s1),len(s2)):
            l = i - len(s1)
            s2_freq[s2[l]] -= 1

            if s2_freq[s2[l]] <= 0:
                s2_freq.pop(s2[l])
            s2_freq[s2[i]] += 1
            if s1_freq == s2_freq:
                return True
        return False

