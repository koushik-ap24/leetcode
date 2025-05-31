from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ## Constraints:
        # there will be at least one stone
        # all stones will have positive weights
        # All stones will have weight > 0

        ## Approach:
        # The trick here is to recognise that this is actually a subset sum problem
        # If we have a pile = sum(stones) // 2, we know the other pile will have the same value
        # So we can smash them together in any order and get the minimum possible value remaining
        # So the goal is to find the largest subset <= sum(stones) // 2, which is a bounded knapsack problem since we can only use each stone once

        cache = {}
        sumWeight = sum(stones)
        target = sumWeight // 2
        def dfs(i, total):
            if total > target:
                return 0
            
            if total == target or i == len(stones):
                return total
            
            if (i,total) in cache:
                return cache[(i,total)]
            
            
            cache[(i,total)] = max(dfs(i+1, total+stones[i]), dfs(i+1, total))
            return cache[(i,total)]

        optPile = dfs(0,0)
        remaining = sumWeight - optPile
        return remaining - optPile