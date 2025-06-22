class TicTacToe:
    ## Approach: Hash Map
    ## TC: O(1) for each move, SC: O(n), where n is the size of the board.
    # We can use a dictionary to keep track of the counts of each player in each row, column, and diagonal.
    # We can also use a set to keep track of the diagonals that have been played.
    def __init__(self, n: int):
        self.rows = {i: [0]*2 for i in range(n)}
        self.cols = {i: [0]*2 for i in range(n)}
        self.diags = {i: [0]*2 for i in range(2)}
        self.diag0 = set()
        self.diag1 = set()
        self.n = n
        col = 0
        for row in range(n):
            self.diag0.add((row,col))
            self.diag1.add(((n-row-1,col)))
            col += 1

    def move(self, row: int, col: int, player: int) -> int:
        ## Add to row
        if self.rows[row][player-1] == self.n-1 or self.cols[col][player-1] == self.n-1:
            return player
        self.rows[row][player-1] += 1
        self.cols[col][player-1] += 1

        ## Add to diagonal
        if (row,col) in self.diag0:
            self.diags[0][player-1] += 1
            if self.diags[0][player-1] == self.n:
                return player
        
        if (row,col) in self.diag1:
            self.diags[1][player-1] += 1
            if self.diags[1][player-1] == self.n:
                return player
        
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)