class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        looser = set()
        lose = {}
        players = set()
        for match in matches:
            w,l = match
            players.update([w,l])
            winner.add(w)
            looser.add(l)
            lose[l] = lose.get(l,0) + 1
        res = [[],[]]
        for e in players:
            if not e in looser:
                res[0].append(e)
        for items in lose.items():
            if items[1] == 1:
                res[1].append(items[0])
        res[0].sort()
        res[1].sort()
        return res
        

