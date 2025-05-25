import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1)
        dp[0] = 0

        for change in range(1, amount+1):
            numCoins = math.inf
            for coin in coins:
                if coin <= change and dp[change-coin] < numCoins:
                    numCoins = dp[change-coin]
            dp[change] = 1 + numCoins
        
        return dp[amount] if dp[amount] != math.inf else -1
        