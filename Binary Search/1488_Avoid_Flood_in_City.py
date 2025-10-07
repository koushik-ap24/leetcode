from collections import defaultdict
from typing import List
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ## Approach: Binary Search + Greedy
        # Whenever we encounter a lake that is already full, we need to find an empty day
        # that is after the last time the lake was filled
        # TC: O(nlogn), SC: O(n)
        
        ans = [-1] * len(rains)
        fullLakes = defaultdict(int)
        emptyDays = SortedList()

        def findEmptyDay(day):
            left = 0
            right = len(emptyDays) - 1
            while left <= right:
                mid = (left + right) // 2
                if emptyDays[mid] >= day:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left


        for i in range(len(rains)):
            lake = rains[i]
            if lake > 0:
                if lake in fullLakes: # At risk of flooding
                    # Need to choose empty day that is after last time the lake is filled
                    lastFilled = fullLakes[lake]
                    idx = findEmptyDay(lastFilled)
                    if idx >= len(emptyDays):
                        return []

                    emptyDay = emptyDays[idx]
                    ans[emptyDay] = lake
                    emptyDays.discard(emptyDays[idx])

                # Update the next day the lake gets filled again
                fullLakes[lake] = i
                ans[i] = -1
            else:
                emptyDays.add(i)
        
        # Arbitrar
        for i in emptyDays:
            ans[i] = 1

        return ans