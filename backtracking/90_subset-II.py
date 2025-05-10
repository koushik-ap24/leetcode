from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include the number
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # Skip duplicates of i
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 
            # At this point we are at the last appearance of the duplicate num, so proces the next element (which is different)
            dfs(i + 1)
        
        
        ## Prefered way
        def backtrack(i, subset):
            res.append(subset.copy())

            for idx in range(i, len(nums)):
                if idx > i and nums[idx] == nums[idx-1]:
                    continue

                subset.append(nums[i])
                backtrack(i, subset)
                subset.pop()    

        dfs(0)
        backtrack(0,[])
        return res