from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        if arraySum % 2 != 0:
            return False
        
        # At this point, the problem boils down to whether a subset can be formed with sum = 1/2 arraySum
        # Can be done top-down via backtracking

        # Backtracking with cache
        cache = {}
        target = int(arraySum/2)
        def dfs(i, currSum):
            if currSum == target:
                return True
            
            if currSum > target or i == len(nums):
                return False
            
            if (i, currSum) in cache:
                return cache[(i,currSum)]
            
            # either include in subset or dont.
            cache[(i,currSum)] = dfs(i+1, currSum + nums[i]) or dfs(i+1, currSum)
            return cache[(i,currSum)]


        return dfs(0, 0)

        # TC: O(n*t), SC: O(n*t)