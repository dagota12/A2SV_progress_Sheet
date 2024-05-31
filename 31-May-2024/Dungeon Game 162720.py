# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon),len(dungeon[0])
        in_bound = lambda r,c: 0<=r<n and 0<=c<m
        dirs = [(1,0),(0,1)]
        visited = [[False]*m for _ in range(n)]
        memo = {}
        def dp(row,col):
            if row == n-1 and col ==m-1:
                return dungeon[-1][-1]
            curr_min = float('-inf')
            if (row,col) not in memo:
                for x,y in dirs:
                    new_r,new_c = row + x,col + y
                    if in_bound(new_r,new_c) and not visited[new_r][new_c]:
                        visited[new_r][new_c] = True
                        curr_min = max(curr_min,min(0,dp(new_r,new_c)))
                        visited[new_r][new_c] = False

                memo[(row,col)] = min(0,curr_min + dungeon[row][col])
            return memo[(row,col)]
        # print()
        ans = dp(0,0)
        return abs(ans) + 1 if ans <= 0 else 1













        # while queue:
        #     pt,row,col = heappop(queue)
        #     print(pt,row,col)
        #     if pt == 0:
        #         ct -= 1
        #     if row == n-1 and col ==m-1:
        #         break
        #     health = min(-pt,health)
        #     for x,y in dirs:
        #         new_r,new_c = row + x,col + y
        #         if in_bound(new_r,new_c) and not visited[new_r][new_c]:
        #             visited[new_r][new_c] = True
        #             heappush(queue,(-(-pt + dungeon[new_r][new_c]),new_r,new_c))
        # print(health,ct)
        # return 0