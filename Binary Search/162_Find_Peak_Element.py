from math import inf
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Approach: Binary search
        # Logic = choose side with higher number due to chance of that being the peak over the smaller side
        # This only works because of the assumption nums[i] != nums[i+1]
        # TC: O(log n), SC: O(1)
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            l = -inf if mid == 0 else nums[mid-1]
            r = -inf if mid == len(nums) - 1 else nums[mid+1]
            if nums[mid] > l and nums[mid] > r:
                return mid
            
            if r > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
