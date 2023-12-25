class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mx =abs(target[0]) + abs(target[1])
        for p in ghosts:
            if (abs(p[0] - target[0]) + abs(p[1] - target[1]))<= mx:
                return False
        return True
        