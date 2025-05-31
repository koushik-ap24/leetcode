from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ## Approach:
        # Notice how this the same as unbounded knapsack (coin change) problem
        # Given unlimited number of coins, find all ways to make change (target)
        # Instead of finding min combinations, you're finding all combinations

        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    break

                dp[i] += dp[i-num]

        return dp[target]
            
