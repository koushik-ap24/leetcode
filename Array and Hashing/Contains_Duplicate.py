from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = []
        for num in nums:
            if num in map:
                return True
            else:
                map.append(num)
        return False
         