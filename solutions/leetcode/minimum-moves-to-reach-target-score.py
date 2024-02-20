class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        inc,dub = 0,0
        while target > 0:
            if maxDoubles > 0 and target > 2:
                if target%2 != 0:
                    inc += 1
                target//=2
                dub += 1
                maxDoubles -= 1
            else:
                inc += target - 1
                break
        return inc + dub

