from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS,COLS = len(board), len(board[0])

        def dfs(row,col):
            if min(row,col) < 0 or row >= ROWS or col >= COLS or board[row][col] != 'X':
                return
            
            board[row][col] = 'O'
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)
            return
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "X":
                    dfs(row,col)
                    res += 1

        return res