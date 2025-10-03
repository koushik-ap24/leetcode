from typing import List

### First encountered in Microsoft Onsite 2025
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ## Approach: Math + Simulation
        # Intuition: The number of diagonals in a n x m matrix is (n + m - 1).
        # Each diagonal can be identified by the sum of its indices (i + j).
        # Odd indexed diagonals are traversed downwards, even indexed diagonals upwards.
        # For even diagonals, start from the bottommost element of the diagonal and move upwards.
        # For odd diagonals, start from the topmost element of the diagonal and move down
        ## TC: O(n*m), SC: O(1)
        res = []
        n,m = len(mat), len(mat[0])
        numDiagonals = (n + m) - 1
        row = col = 0

        for diag in range(numDiagonals):
            if diag % 2 == 0: # Moving up
                row = min(diag, n-1)
                col = diag - row
                while row >= 0 and col < m:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
    
            else: # Moving down
                col = min(diag, m-1)
                row = diag - col
                while col >= 0 and row < n:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1 

        return res