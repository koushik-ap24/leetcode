from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Method 1: recursion
        def dfs(hold, idx, total):
            if idx >= len(prices):
                return total
            
            profit = 0
            
            # buy if we are not holding any coin yet
            if not hold:
                profit = dfs(True, idx+1, total-prices[idx])
            else:
                profit = dfs(False, idx+2, total+prices[idx])
            
            # we can always choose to skip day regardless of if we hold or not
            return max(profit, dfs(hold, idx+1, total))
        
        return dfs(False, 0, 0)

        ## Method 2 -> Top-Down DP (memoization using cache)
        cache = {}
        def dfs(idx, hold):
            if idx >= len(prices):
                return 0
            if (idx, hold) in cache:
                return cache[(idx, hold)]
            
            skip = dfs(idx + 1, hold)
            if hold:
                sell = prices[idx] + dfs(idx + 2, False)
                cache[(idx, hold)] = max(sell, skip)
            else:
                buy = -prices[idx] + dfs(idx + 1, True)
                cache[(idx, hold)] = max(buy, skip)
            return cache[(idx, hold)]
        
        return dfs(0, False)
