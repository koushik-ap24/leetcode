from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if i == 0 or nums[i] != nums[i-1]:
                candidateTarget = target - nums[i]
                candidate = [nums[i]]

                ## 3 sum approach
                j = i + 1
                while j < len(nums):
                    if j == i + 1 or nums[j] != nums[j-1]:
                        candidate.append(nums[j])
                        candidateTarget -= nums[j]
                        l = j + 1
                        r = len(nums) - 1
                        while l < r:
                            total = nums[l] + nums[r]
                            if total == candidateTarget and (l == j + 1 or nums[l] != nums[l-1]) and (r == len(nums)-1 or nums[r] != nums[r+1]):
                                copy = candidate.copy()
                                copy.append(nums[l])
                                copy.append(nums[r])
                                res.append(copy)
                            if total <= candidateTarget:
                                l += 1
                            
                            if total >= candidateTarget:
                                r -= 1
                            
                        candidate.pop()
                        candidateTarget += nums[j]
                    j += 1
            i += 1
        
        return res