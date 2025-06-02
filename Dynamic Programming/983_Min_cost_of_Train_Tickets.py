import math
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ## Approach 1: Top-Down DP with Memoization
        cache = {}

        # Rather than use daysLeft, use a loop to do that for you
        def dfs(i):
            if i == len(days):
                return 0
            
            if i in cache:
                return cache[i]
            
            
            res = math.inf
            for cost, duration in zip(costs, [1,7,30]):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1

                res = min(res, cost + dfs(j))

            cache[i] = res
            return res 
        
        return dfs(0)
    
        ## Approach 2: Bottom-Up DP
        n = len(days)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')
            j = i
            for cost, duration in zip(costs, [1,7,30]):
                while j < n and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        
        return dp[0]