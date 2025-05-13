from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ## My solution
        n = len(nums)
        dp = [len(nums)+1] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            minHop = len(nums) + 1
            for j in range(i + 1, end):
                minHop = min(minHop, 1 + dp[j])
            dp[i] = minHop
        return dp[0]