from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## Approach 1: Hash Set
        # TC: O(n), SC: O(n)
        # numSet = set()
        # for num in nums:
        #     if num in numSet:
        #         return num
        #     numSet.add(num)

        ## Possible to improve to TC: O(n), SC: O(1) solution
        ## Approach: Negative Marking
        # Use the array itself as a set for each number
        # Mark each number's corresponding index (0-based) as negative
        # If that element at that index is negative, then we know this number has been seen before, so return it.
        # nums = [1,3,-4,2,2]
        # range =[1,2,3,4]
        n = len(nums)
        for i in range(n):
            position = nums[abs(nums[i]) - 1]
            if position < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * -1

        
        return -1