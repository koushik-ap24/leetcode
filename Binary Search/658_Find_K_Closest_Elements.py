import bisect
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ## Approach 1: Binary Search
        # Find the position where x would fit in the sorted array
        # and then expand outwards to find the k closest elements.
        # TC: O(log n + k log k), SC: O(k)
        l, r = bisect.bisect_left(arr, x), bisect.bisect_right(arr, x)

        res = []
        for i in range(l, r):
            res.append(arr[i])
        
        l -= 1
        while len(res) < k:
            if r >= len(arr) or (l >= 0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        
        res.sort()
        return res[:k]
    
        ## Approach 2: Binary search with sliding window
        # Binary search to find the left boundary of the window
        # TC: O(log(n-k)), SC: O(k)
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            # Compare the distances of the ends of the window
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        # Slice the k elements from the left index
        return arr[left:left + k]