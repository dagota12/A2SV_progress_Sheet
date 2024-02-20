class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        same_color = defaultdict(int)
        for a in answers:
            same_color[a] += 1
        count = 0
        for k,v in same_color.items():
            count += ceil(v/(k+1)) *(k+1)
        return count