class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = defaultdict(int)
        for i in range(k):
            freq[blocks[i]] += 1
        min_white = freq.get("W",0)
        
        for r in range(k,len(blocks)):
            left = r - k
            freq[blocks[left]] -= 1
            freq[blocks[r]] += 1
            min_white = min(min_white,freq["W"])
            
        return min_white


        
        