from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Approach: Could be similar to subarray sum equals k
        oddCount = defaultdict(int)
        oddCount[0] = 1
        numOdd = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                numOdd += 1
            
            diff = numOdd - k
            res += oddCount.get(diff, 0)
            oddCount[numOdd] += 1
        
        return res