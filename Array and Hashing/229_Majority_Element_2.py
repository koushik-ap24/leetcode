from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## Approach1: HashMap
        ## TC: O(n), SC: O(n)
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        res = []
        threshold = len(nums) // 3
        for element,count in countMap.items():
            if count > threshold:
                res.append(element)
            
        return res

        ## Optmised approach: HashMap + Voting algorithm
        ## TC: O(n), SC: O(1)
        ## Note: This approach is not optimal for this problem, but it is a good exercise
        ## The idea is to maintain a hashmap of at most 2 elements and their counts
        count = defaultdict(int)
        threshold = len(nums) // 3
        for num in nums:
            count[num] += 1

            if len(count) < 3:
                continue
            
            ## Never modify hashmap as you are looping through it!
            newCount = defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    newCount[n] = c - 1
            count = newCount
        
        res = []
        for element in count:
            if nums.count(element) > threshold:
                res.append(element)
        
        return res