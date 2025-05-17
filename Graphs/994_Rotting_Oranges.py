from collections import deque
from typing import List


# Pretty much identical to walls and gates
# Multi-BFS from each rotten fruit, and keep track of the number of rotten fruits currently
# If it is same as total fruits, then return time. Otherwise return -1 due to impossible outcome.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        numFruits = 0

        def addFruit(row, col):
            if (min(row, col) < 0 or row == ROWS or col == COLS or 
                grid[row][col] != 1):
                return
            
            # Mark as visited but its not yet rotten
            print(f"row: {row}, col: {col}")
            grid[row][col] = 3
            queue.append([row,col])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0:
                    numFruits += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        # If every fruit is rotten
        if len(queue) == numFruits:
            return 0
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = 2
                numFruits -= 1
                addFruit(row, col+1)
                addFruit(row, col-1)
                addFruit(row+1, col)
                addFruit(row-1, col)
        
        if numFruits != 0:
            return -1
        
        return time
