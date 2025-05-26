from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ## Initial solution (Recursion)
        def dfs(idx, currSum):
            if idx == len(nums) and currSum == target:
                return 1
            if idx == len(nums) and currSum != target:
                return 0
            
            # For each num, we can either add or subtract it
            return dfs(idx+1, currSum + nums[idx]) + dfs(idx+1, currSum - nums[idx])
        

        return dfs(0, 0)