from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    ## Constraints:
    # Matrix can have different number of rows and columns
    # Matrix can be empty
    # All numbers will only be positive

        if len(matrix) == 0:
            return 0
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = {}

        def dfs(row, col, prev):
            if (min(row, col) < 0 or row == ROWS or col == COLS or matrix[row][col] <= prev):
                return 0
            
            if (row, col) in visited:
                return visited[(row,col)]
            
            cell = matrix[row][col]
            
            visited[(row,col)] = 1 + max(dfs(row-1, col, cell),
                        dfs(row+1, col, cell),
                        dfs(row, col+1, cell),
                        dfs(row, col-1, cell))
                        
            return visited[(row,col)]

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited:
                    # Since starting from this cell, there is no previous
                    res = max(res, dfs(row, col, -1))
        return res