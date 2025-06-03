from typing import List

class Solution:
    # Approach: Spiral Order interative traversal

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        res = []

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def in_bounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited

        row, col = 0, 0
        dir_idx = 0  # Start with right direction

        # Only iterate for the number of elements in the matrix.
        for _ in range(ROWS * COLS):
            res.append(matrix[row][col])
            visited.add((row, col))

            # Try to move in the current direction
            next_row = row + directions[dir_idx][0]
            next_col = col + directions[dir_idx][1]

            # If invalid, rotate direction
            if not in_bounds(next_row, next_col):
                dir_idx = (dir_idx + 1) % 4
                next_row = row + directions[dir_idx][0]
                next_col = col + directions[dir_idx][1]

            row, col = next_row, next_col

        return res