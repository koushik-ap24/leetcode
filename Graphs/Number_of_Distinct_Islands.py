from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        paths = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col, path, direction):
            if (min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] == 0):
                return
            
            grid[row][col] = 0
            path.append(direction)
            dfs(row+1, col, path, "D")
            dfs(row-1, col, path, "U")
            dfs(row, col+1, path, "R")
            dfs(row, col-1, path, "L")
            
            path.append("B")
            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    path = []
                    dfs(row, col, path, "S")
                    paths.add(''.join(path))
        
        return len(paths)