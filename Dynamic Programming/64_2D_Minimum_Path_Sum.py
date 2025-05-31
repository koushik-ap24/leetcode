import math
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ## Constraints:
        # Numbers will only be non negative
        
        ## Approach 1 - top-down
        ROWS = len(grid)
        COLS = len(grid[0])
        cache = {}

        def dfs(row, col):
            if min(row,col) < 0 or row == ROWS or col == COLS:
                return math.inf
            
            if row == ROWS-1 and col == COLS-1:
                return grid[row][col]
            
            if (row,col) in cache:
                return cache[(row,col)]
            
            cache[(row,col)] = grid[row][col] + min(dfs(row+1, col), dfs(row, col+1))
            return cache[(row,col)]
        
        return dfs(0,0)

        ## Approach 2 -> bottom up

        dp = [[math.inf] * (COLS+1) for _ in range(ROWS+1)]
        dp[ROWS][COLS-1] = dp[ROWS-1][COLS] = 0
        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
        return dp[0][0]