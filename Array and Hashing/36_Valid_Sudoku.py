from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        subgridMap = defaultdict(set)
        ROWS,COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != ".":
                    quadrant = (row // 3) * 3 + (col // 3)
                    num = board[row][col]
                    if ((row in rowMap and num in rowMap[row]) or
                        (col in colMap and num in colMap[col]) or
                        (quadrant in subgridMap and num in subgridMap[quadrant])):
                        return False
                    
                    rowMap[row].add(num)
                    colMap[col].add(num)
                    subgridMap[quadrant].add(num)
            
        return True

