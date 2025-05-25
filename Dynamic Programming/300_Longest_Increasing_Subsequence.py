from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # For first element, longest subsequence is just itself
        dp[0] = 1
        maxLIS = 1

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxLIS = max(maxLIS, dp[i])

        return maxLIS