from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # Approach: DFS with memoization (top-down DP)
        # Intuition: At each cell, we can either go right or down
        # If we hit a cell with a mirror, we have to change direction
        # We use memoization to store the number of unique paths from each cell
        ## TC: O(m*n), SC: O(m*n) for the cache
        ROWS, COLS = len(grid), len(grid[0])
        MOD = 10**9 + 7
        cache = {}

        def dfs(row, col, parent):
            if min(row, col) < 0 or row >= ROWS or col >= COLS:
                return 0
            
            if row == ROWS-1 and col == COLS-1:
                return 1
            
            if (row,col) in cache:
                return cache[(row,col)]
            
            if grid[row][col] == 1:
                # Check the direction of incidence
                if row == parent[0] and col == parent[1] + 1:
                    return dfs(row+1, col, (row,col)) % MOD
                else:
                    return dfs(row, col+1, (row,col)) % MOD
            
            cache[(row,col)] = (dfs(row, col+1, (row,col)) + dfs(row+1, col, (row,col))) % MOD
            return cache[(row,col)]
        
        return dfs(0, 0, (0,0))