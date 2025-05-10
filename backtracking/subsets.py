from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # My solution -> iterative
        result = [[]]
        for num in nums:
            subsets = []
            for subset in result:
                # newSet = subset.copy()
                # newSet.append(num)
                ## Use array addition to preserve original length and not cause infinite loop!
                subset = subset + [num]
                subsets.append(subset)
            result.extend(subsets)
        
        return result

        ## Solution using backtracking
        res = []

        def dfs(i, subset):
            res.append(subset.copy())

            for idx in range(i, len(nums)):
                subset.append(nums[idx])
                dfs(idx+1, subset)
                subset.pop()    

        dfs(0, [])
        return res


