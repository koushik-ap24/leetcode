from collections import defaultdict
from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        ## Approach: Hashing with Sorting
        # Get the access times for each employee and store them in a map
        # Sort the access times for each employee and check if there are 3 consecutive accesses within an hour using sliding window
        # TC: O(n log n), SC: O(n)
        accessMap = defaultdict(list)
        for employee, time in access_times:
            accessMap[employee].append(time)
        
        res = []
        for employee, times in accessMap.items():
            times.sort()
            if len(times) < 3:
                continue
            
            l,r = 0, 1
            while r < len(times):
                hourRight = times[r][0:2]
                while (times[l][0:2] != hourRight and int(times[r])-int(times[l]) >= 100):
                    l += 1
                
                if (r - l + 1) == 3:
                    res.append(employee)
                    break
                
                r += 1
        
        return res