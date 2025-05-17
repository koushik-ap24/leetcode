from typing import List

class Solution:
    # Start dfs from the border cells
    # Look for cells that have values higher than the current cell (that means water can flow from that node to the current node, so its valid and we can continue looking for more compatible nodes)
    # We look for higher cells since we start from the ocean rather than going towards the ocean (working backwards )
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r, c) in visited or heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r+dr, c+dc, visited, heights[r][c])

            
        # do border cols first
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        # # do border rows next
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        # find intersection between sets
        intersection = pacific.intersection(atlantic)
        return list(intersection)
