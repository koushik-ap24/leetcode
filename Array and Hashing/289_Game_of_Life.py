class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ## Approach 1: Copy state then apply neighbor rules
        # TC: O(m*n), SC: O(m*n)
        m,n = len(board), len(board[0])
        copy = [[0] * n for _ in range(m)]

        def inbounds(row,col):
            return (row >= 0 and row < m and col >= 0 and col < n)
        
        for row in range(m):
            for col in range(n):
                copy[row][col] = board[row][col]
        
        directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        for row in range(m):
            for col in range(n):
                numLive = 0
                for x, y in directions:
                    newX = row + x
                    newY = col + y
                    if inbounds(newX, newY):
                        numLive += copy[newX][newY]
                
                if copy[row][col] == 1 and (numLive < 2 or numLive > 3):
                    board[row][col] = 0
                elif copy[row][col] == 0 and numLive == 3:
                    board[row][col] = 1

        ## Approach 2: Inplace state change using tuples
        # TC: O(m*n), SC: O(1)
        for row in range(m):
            for col in range(n):
                board[row][col] = (board[row][col], board[row][col])
        
        directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        for row in range(m):
            for col in range(n):
                numLive = 0
                for x, y in directions:
                    newX = row + x
                    newY = col + y
                    if inbounds(newX, newY):
                        numLive += board[newX][newY][0]
                
                if board[row][col][0] == 1 and (numLive < 2 or numLive > 3):
                    board[row][col] = (board[row][col][0], 0)
                elif board[row][col][0] == 0 and numLive == 3:
                    board[row][col] = (board[row][col][0], 1)
        
        for row in range(m):
            for col in range(n):
                board[row][col] = board[row][col][1]
