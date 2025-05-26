from collections import deque

## My soln: TC = (m*n), SC = (m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([0]*n) for _ in range(m)]
        dp[m-1][n-1] = 1
        visited = set()
        queue = deque([(m-1, n-1)])

        while queue:
            row, col = queue.popleft()
            if (row, col) in visited:
                continue

            visited.add((row, col))
            if row < m-1:
                dp[row][col] += dp[row+1][col]
            if col < n-1:
                dp[row][col] += dp[row][col+1]

            ## Add next cells
            if row - 1 >= 0:
                queue.append((row-1,col))
            
            if col - 1 >= 0:
                queue.append((row,col-1))
        
        return dp[0][0]
    
        ## better solution (no need to use queue and visited!)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                dp[row][col] += dp[row+1][col] + dp[row][col+1]
        
        return dp[0][0]

                

        