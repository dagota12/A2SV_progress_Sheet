class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dir, rad = deque(),deque()
        for i in range(len(senate)):
            if senate[i] == 'D':
                dir.append(i)
            else:
                rad.append(i)
        idx = len(senate)
        while dir and rad:
            if dir[0] < rad[0]:
                dir.append(idx)
            else:
                rad.append(idx)
            idx += 1
            rad.popleft()
            dir.popleft()
        return "Radiant" if rad else "Dire"
        
