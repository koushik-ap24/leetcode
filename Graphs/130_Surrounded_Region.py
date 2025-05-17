from typing import List

## Work backwards -> find all "O"s that you can reach from border "O"s
## All the ones that you can't reach, mark them as surrounded ("X")
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if (min(row, col) < 0 or row == ROWS or col == COLS or 
                board[row][col] != "O"):
                return
            
            board[row][col] = "!"
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)
        
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS-1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS-1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "!":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"