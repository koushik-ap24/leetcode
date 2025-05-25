from typing import List

## Maintain max and min product ending at previous index since we have -ve numbers.
## Can be space-optimised by using variables instead of dp array, since we only care about the previous index (and not any values before it)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpMax = [1] * len(nums)
        dpMin = [1] * len(nums)
        dpMax[0] = dpMin[0] = nums[0]
        maxProd = nums[0]

        for i in range(1, len(nums)):
            dpMax[i] = max(nums[i], dpMax[i-1]*nums[i], dpMin[i-1]*nums[i])
            dpMin[i] = min(nums[i], dpMax[i-1]*nums[i], dpMin[i-1]*nums[i])
            maxProd = max(maxProd, dpMax[i])
        
        return maxProd