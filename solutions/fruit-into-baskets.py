class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0
        max_len = 0

        for r in range(len(fruits)):
            freq[fruits[r]] += 1
            while len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] <= 0:
                    freq.pop(fruits[l])
                l+=1
            max_len = max(max_len, r - l + 1)
        return max_len  
