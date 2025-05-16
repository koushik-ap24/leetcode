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

        ## Greedy Solution
        # Process the furthest you can reach at any point using 2 pointers
        # 2 pointers allows you to process furthest in linear time
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res