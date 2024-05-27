# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stoneSet = set(stones)
        visited = set()
        def dfs(value,jump):
            if (value+jump not in stoneSet) or ((value,jump) in visited):
                return False
            if value+jump == stones[n-1]:
                return True
            visited.add((value,jump))
            return dfs(value+jump,jump) or dfs(value+jump,jump-1) or dfs(value+jump,jump+1)
        return dfs(stones[0],1)
            
            
            
