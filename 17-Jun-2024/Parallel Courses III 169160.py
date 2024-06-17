# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph =  defaultdict(list)
        deg = [0]*n
        req = [0]*n
        for u,v in relations:
            u-=1;v-=1
            graph[u].append(v)
            deg[v] += 1
        # print(graph)
        queue = deque([i for i in range(n) if deg[i] == 0])
        # print(queue)
        for i in range(n):
            if deg[i] == 0:
                req[i] = time[i]
        while queue:
            node = queue.popleft()
            for neg in graph[node]:
                deg[neg] -= 1
                # print(node+1,neg+1,deg[neg])
                req[neg] = max(req[neg],req[node])
                # print(req)
                if deg[neg] == 0:
                    req[neg] +=  time[neg]
                    queue.append(neg)
        # print(req)
        return max(req)
