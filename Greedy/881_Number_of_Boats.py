import bisect
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ## Approach: Sorting + 2 pointer (greedy)
        # Sort array by weight in non-decreasing order
        people.sort()
        res = 0

        # Find largest element <= limit
        right = min(len(people)-1, bisect.bisect_left(people, limit))
        res += (len(people) - (right+1))

        # Greedy 2-pointer approach
        left = 0
        while left <= right:
            res += 1
            weightSum = people[left] + people[right]
            if weightSum <= limit:
                left += 1
            
            right -= 1
        
        return res