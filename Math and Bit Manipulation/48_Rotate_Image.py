from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for col in range(n):
            topRow, botRow = 0, n-1
            while topRow < botRow:
                matrix[topRow][col], matrix[botRow][col] = matrix[botRow][col], matrix[topRow][col]
                topRow += 1
                botRow -= 1
        
        diagRow = diagCol = 0
        while diagRow < n and diagCol < n:
            leftRow = rightRow = diagRow
            leftCol = rightCol = diagCol
            while leftRow < n and rightCol < n:
                matrix[leftRow][leftCol], matrix[rightRow][rightCol] = matrix[rightRow][rightCol], matrix[leftRow][leftCol]
                leftRow += 1
                rightCol += 1
            
            diagRow += 1
            diagCol += 1
    