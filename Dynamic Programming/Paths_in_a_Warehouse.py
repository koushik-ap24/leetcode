from typing import List
from collections import deque


def numPaths(warehouse: List[List[int]]) -> int:
    ## Approach: Dynamic Programming + BFS
    # Start from bottom right corner and move to top left corner
    # Very similar to unique paths problem
    # TC: O(m*n), SC: O(m*n)
    
    ROWS, COLS = len(warehouse), len(warehouse[0])
    dp = [[0] * COLS for _ in range(ROWS)]
    # Base case
    dp[ROWS-1][COLS-1] = 1
    visited = set()
    queue = deque([(ROWS-1, COLS-1)])
    
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited or warehouse[row][col] == 0:
            continue
        
        visited.add((row,col))
        # 2 directions - down or right
        # Down: row < ROWS - 1
        if row < ROWS - 1:
            dp[row][col] += dp[row+1][col]
        
        if col < COLS - 1:
            dp[row][col] += dp[row][col+1]
        
        # Add new cells for consideration
        if row - 1 >= 0 and warehouse[row-1][col] != 0:
            queue.append((row-1, col))
        if col - 1 >= 0 and warehouse[row][col-1] != 0:
            queue.append((row, col-1))
    
    return dp[0][0]

print(numPaths([[1,1,1,1], [1,1,1,1], [1,1,1,1]])) #10
print(numPaths([[1,1], [0,1]])) #1
print(numPaths([[1,1,0,1], [1,1,1,1]])) #2