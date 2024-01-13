class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        vowels = "aeiou"
        count = 0
        for j in range(k):
            if s[j] in vowels:
                count += 1
            hm[e] += 1
        temp = count
        for i in range(k,len(s)):
            left_el = s[i-k]
            hm[left_el] -= 1
            if left_el in vowels:
                temp -= 1
            if hm[left_el] <= 0:
                hm.pop(left_el)
            
            if s[i] in vowels:
                temp += 1
            count = max(count,temp)
        return count
            


            

