from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort() 
        
        ## Approach 1: Binary search
        # For each house, binary search for the closest heater on the left and right
        # Take the min distance of the two and update the result if its larger than previous
        # TC: O(n log m), SC: O(1) where n is number of houses and m is number of heaters
        def beforeSearch(house):
            heaterBefore = heaters[0]
            left = 0
            right = len(heaters) - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] <= house:
                    heaterBefore = max(heaterBefore, heaters[mid])
                    left = mid + 1
                else:
                    right = mid - 1
            
            return heaterBefore
        
        def afterSearch(house):
            heaterAfter = heaters[-1]
            left = 0
            right = len(heaters) - 1
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] >= house:
                    heaterAfter = min(heaterAfter, heaters[mid])
                    right = mid - 1
                else:
                    left = mid + 1
            
            return heaterAfter

        res = 0
        for house in houses:
            # Perform 2 binary searches
            minHouseRadius = min(abs(house - beforeSearch(house)), abs(afterSearch(house) - house))
            res = max(res, minHouseRadius)
        
        return res