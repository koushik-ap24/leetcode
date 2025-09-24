import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ## Assumptions:
        # 1 <= k < len(nums)
        # len(nums) >= 1
        # Float error is acceptable

        l = r = 0
        res = -math.inf
        rollingSum = 0
        while r < len(nums):
            rollingSum += nums[r]
            if (r-l+1) == k:
                res = max(res, rollingSum)
                rollingSum -= nums[l]
                l += 1
            r += 1
        
        return res/k