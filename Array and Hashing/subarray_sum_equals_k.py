from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        # Base case, to set 0 diff to 1
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res