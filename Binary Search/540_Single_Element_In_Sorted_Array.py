from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ## Approach: Binary Search
        # Check for the middle element and its neighbors
        # if the middle element is equal to its left or right neighbor, 
        # we can determine which half of the array to search next based on the length of the half without the 
        # same element as the middle.
        # TC: O(log n), SC: O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid - 1 >= 0 and nums[mid-1] == nums[mid]:
                candidate = mid + 1 if (r-mid) % 2 else mid - 2
            elif mid + 1 < len(nums) and nums[mid+1] == nums[mid]:
                candidate = mid - 1 if (mid - l) % 2 else mid + 2
            else:
                return nums[mid]
            
            if candidate < mid:
                r = candidate
            else:
                l = candidate
        
        return nums[l]