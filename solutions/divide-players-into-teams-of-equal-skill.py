class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        p1,p2 = 0, len(skill) - 1
        s = skill[p1] + skill[p2]
        while p1 < p2:
            sk = skill[p1] + skill[p2]
            if s and sk != s:
                return -1
            chemistry += skill[p1] * skill[p2]
            p1 += 1
            p2 -= 1
        return chemistry

