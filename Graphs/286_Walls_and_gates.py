from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # My solution -> run bfs for each room encountered
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(row, col):
            q = deque([(row, col)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[row][col] = True
            steps = 0
            while q:
                # Keep track of level by the length of the queue.
                # When all nodes in queue have been replaced, then we have explored all neighbours so moving up one level
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and 
                            not visit[nr][nc] and grid[nr][nc] != -1
                        ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)

        ##################################################################################################
        ## Better solution, use multisource BFS from gates rather than rooms!
        ## WORK BACKWARDS
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        def addCell(row, col):
            if (min(row, col) < 0 or row == ROWS or col == COLS or
                grid[row][col] < INF
            ):
                return
            q.append([row, col])
            # Mark it as visited by changing it to anything besides INF
            grid[row][col] = 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    # Only add gates to queue first
                    q.append([row, col])

        dist = 0
        # Do BFS from each gate at the same time (each layer is done at the same time)
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                # Update the cell with the actual shortest distance
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1