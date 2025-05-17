from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.area = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            self.area += 1
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row-1,col)
            dfs(row+1, col)

            ## Another cleaner way to do it (rather than using instance variables)
            return 1 + dfs(row, col+1) + dfs(row, col-1) + dfs(row-1, col) + dfs(row+1, col)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    maxArea = max(maxArea, self.area)
                    self.area = 0
        return maxArea