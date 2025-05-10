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
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


