from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()

        for i in range(len(nums)):
            # Avoid duplicates in first position
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            leftP = i+1
            rightP = len(nums) - 1
            while leftP < rightP:
                if nums[leftP] + nums[rightP] == target:
                    res.append([nums[i], nums[leftP], nums[rightP]])
                    leftP += 1
                    rightP -= 1
                    # To ensure we only get unique 2 sums, either left or right has to be unique all the time!
                    while nums[leftP] == nums[leftP-1] and leftP < rightP:
                        leftP += 1
                elif nums[leftP] + nums[rightP] > target:
                    rightP -= 1
                else:
                    leftP += 1
        
        return res