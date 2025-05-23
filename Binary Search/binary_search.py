import math
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftP = 0
        rightP = len(nums) - 1
        result = -1
        while leftP <= rightP:
            diff = rightP - leftP
            mid = math.floor(diff/2)
            index = leftP + mid
            if (nums[index]) == target:
                result = index
                break
            elif (nums[index]) > target:
                rightP = index - 1
            else:
                leftP = index + 1
        
        return result