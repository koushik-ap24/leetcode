from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # for num,count in count.items():
        #     freq[count].append(num)
        
        # for i in range(len(freq)-1, 0, -1):
        #     if len(freq[i]) > 0:
        #         return freq[i][0]

        # TC -> O(n)
        # SC -> O(n)

        result = maxCount = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > maxCount:
                maxCount = count[num]
                result = num
        
        return result