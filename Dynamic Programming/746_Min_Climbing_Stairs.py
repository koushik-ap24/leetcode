from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        # Since you can start at either first or second stair, the cost to get to them is 0
        dp[0] = 0
        dp[1] = 0
        for i in range (2, len(dp)):
            dp[i] = min((dp[i-2] + cost[i-2]), (dp[i-1] + cost[i-1]))
        
        return dp[-1]