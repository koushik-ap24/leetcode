from typing import List

# Run DFS/BFS on grid. Anytime a contiguous 1 is reached, mark it as 'visited' by setting it to 0.
# When 1 is found, run DFS on all adjacent nodes and mark them as visited if any of them are 1 as well.
# Continue until all nodes have been traversed
# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(row, col):
            ## My solution
            # grid[row][col] = "0"
            # if grid[row][min(col+1, len(grid[0])-1)] == "1":
            #     dfs(row, col+1)
            # if grid[min(row+1, len(grid)-1)][col] == "1":
            #     dfs(row+1, col)
            # if grid[max(row-1, 0)][col] == "1":
            #     dfs(row-1, col)
            # if grid[row][max(col-1, 0)] == "1":
            #     dfs(row, col-1)

            ## More efficient solution:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] != "1":
                return
            
            grid[row][col] = "0"
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row-1,col)
            dfs(row+1, col)
            
            return
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row,col)
                    islands += 1
        return islands