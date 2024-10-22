# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        n,m = len(grid),len(grid[0])
        in_bound = lambda r,c: 0 <= r < n and 0<= c < m
        dist = {(i,j): float("inf") for i in range(n) for j in range(m)}
        dist[(0,0)] = 0
        queue = [(0,0,0)] # priority queue (dist,row,col)
        visited = set()
        while queue:
            d,row,col = heappop(queue)
            # print(f"{d},r:{row},c:{col}")
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for x,y in dirs:
                new_r,new_c = row + x,col + y
                if in_bound(new_r,new_c):
                    new_dist = d + grid[new_r][new_c]
                    # print(f"d:{d}, {new_r},{new_c}")
                    if new_dist < dist[(new_r,new_c)]:
                        dist[(new_r,new_c)] = new_dist
                        heappush(queue,[new_dist,new_r,new_c])
        # print(dist)
        return dist[(n-1,m-1)]

