import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ## Approach: Sort potions and use binary search for each spell to find the minimum potion needed
        ## TC: O(n log n + m log n), SC: O(1) if we ignore output array
        potions.sort()
        n = len(potions)
        res = []

        for spell in spells:
            target = math.ceil(success/spell)

            # binary search
            left = 0
            right = n-1
            while left <= right:
                mid = (left+right)//2
                if potions[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            validPairs = 0
            if left < n:
                validPairs = (n - left)
            
            res.append(validPairs)
        
        return res