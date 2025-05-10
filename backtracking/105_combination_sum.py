from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        ## My modified solution
        def dfs(currSum, i, path):
            if currSum > target:
                return

            if currSum == target:
                res.append(path.copy())
                return
            
            for idx in range(i, len(nums)):
                path.append(nums[idx])
                # Explore all possible valid paths that include this candidate.
                dfs(currSum + nums[idx], idx, path)
                # we need to pop as we have now considered all valid paths with this candidate, so move on to next candidate
                path.pop() 
        
        # start with the first element as the candidate.
        dfs(0, 0, [])
        
        return res
    

    ## Simpler approach
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currSum, i, path):
            if currSum == target:
                res.append(path.copy())
                return
            if i >= len(nums) or currSum > target:
                return

            path.append(nums[i])
            dfs(currSum + nums[i], i, path)
            path.pop()
            dfs(currSum, i + 1, path)

        dfs(0, 0, [])
        return res
