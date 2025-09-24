from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if grid[row][col] == 0 or (row,col) in visited:
                return 0
            
            visited.add((row,col))
            val = 0
            for i in range(COLS):
                if grid[row][i] == 1 and (row,i) not in visited:
                    val += dfs(row, i)
            
            for j in range(ROWS):
                if grid[j][col] == 1 and (j,col) not in visited:
                    val += dfs(j, col)
            
            return val + 1
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    temp = dfs(row,col)
                    if temp > 1:
                        res += temp
        
        return res

