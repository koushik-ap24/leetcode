from typing import List

## CLassic Unbounded Knapsack problem
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        ## Num cols = amount + 1
        ## Num rows = n + 1 (account for no coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        ## Base cases
        for i in range((n+1)):
            dp[i][0] = 1
        
        for row in range(1, n+1):
            for col in range(1, amount+1):
                ## Pick coin if it is <= amount
                if coins[row-1] <= col:
                    dp[row][col] += dp[row][col - coins[row-1]]
                
                # Dont pick coin (either way) (you can always choose to not pick the coin!)
                dp[row][col] += dp[row-1][col]
        
        return dp[n][amount]
