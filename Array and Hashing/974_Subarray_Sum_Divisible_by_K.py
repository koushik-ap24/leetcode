from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixCount = defaultdict(int)
        prefixCount[0] = 1
        prefixSum = 0
        res = 0

        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            res += prefixCount[remainder]
            prefixCount[remainder] += 1
        
        return res