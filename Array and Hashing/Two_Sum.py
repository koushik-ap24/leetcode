from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []

        for i in range(len(nums)):
            target_num = abs(target - nums[i])
            if seen.get(target_num, -1) != -1:
                result.append(seen.get(target_num))
                result.append(i)
                break
        else:
            seen[nums[i]] = i
        
        return result