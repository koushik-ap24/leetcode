from collections import defaultdict, deque
from typing import List
from typing import Tuple


class Solution:
    # TC: O(m*n), SC: O(m*n)
    def mazeNavigate(self, maze: List[List[int]], start: Tuple[int, int]):
        res = defaultdict(list)
        ancestors = defaultdict(tuple)
        treasures = []
        visited = set()
        queue = deque([])
        queue.append(start)

        while queue:
            node = queue.popleft()
            if node[0] < 0 or node[0] >= len(maze) or node[1] < 0 or node[1] >= len(maze[0]) or node in visited:
                continue

            if maze[node[0]][node[1]] == "T":
                treasures.append(node)
            
            visited.add(node)
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                neighbour = (node[0]+x, node[1]+y)
                if neighbour not in visited:
                    queue.append(neighbour)
                    ancestors[neighbour] = node

        ## Construct path for each treasure
        for treasure in treasures:
            node = treasure
            while node != start:
                res[treasure].insert(0, node)
                node = ancestors[node]
            res[treasure].insert(0, start)

        return res
    
maze = [
    [0, 0, "T", 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, "T", 1, "T"],
    [0, "T", 0, 0, 0]
]
start = (0, 0)
sol = Solution()
print(sol.mazeNavigate(maze, start))
