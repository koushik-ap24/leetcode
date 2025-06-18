from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)

        if start >= len(nums) or nums[start] != target or nums[end-1] != target:
            return [-1,-1]
        
        return [start,end-1]