from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Approach: DFS to identify the two islands, then multi-source BFS from one island to another
        # TC: O(n*m), SC: O(n*m)

        def dfs(x, y, islandSet, otherSet):
            if min(x,y) < 0 or max(x,y) >= len(grid) or grid[x][y] == 0 or (x,y) in islandSet or (x,y) in otherSet:
                return
            
            islandSet.add((x,y))
            dfs(x+1, y, islandSet, otherSet)
            dfs(x-1, y, islandSet, otherSet)
            dfs(x, y+1, islandSet, otherSet)
            dfs(x, y-1, islandSet, otherSet)

        # Identify connected components
        island1 = set()
        island2 = set()
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    if count == 0:
                        dfs(x,y,island1, island2)
                        count += 1
                    else:
                        dfs(x,y,island2, island1)
        
        # Multi-source BFS from island1 to island2
        # Find shortest path between two connected components
        res = 0
        queue = deque([])
        visited = set()
        for point in island1:
            queue.append(point)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node in visited or min(node[0],node[1]) < 0 or max(node[1], node[0]) >= len(grid):
                    continue
                
                if node in island2:
                    return res-1
                
                visited.add(node)
                for x,y in [(0,1), (1,0), (-1, 0), (0, -1)]:
                    queue.append((node[0] + x, node[1] + y))
            
            res += 1
            
        return -1