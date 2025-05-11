from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(exclude, permutation):
            if len(exclude) == len(nums):
                res.append(permutation.copy())
            
            for i in range(len(nums)):
                if i in exclude:
                    continue
                
                exclude.add(i)
                permutation.append(nums[i])
                dfs(exclude, permutation)
                exclude.remove(i)
                permutation.pop()

        excludeSet = set()
        dfs(excludeSet, [])
        return res