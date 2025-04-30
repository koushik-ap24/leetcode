from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)
        
        # get starting values of sequences (where num - 1 not in hash set)
        startingNums = []
        for num in nums:
            if (num - 1) not in uniqueNums:
                startingNums.append(num)
        
        largestSeq = 0
        currSeq = 0
        currNum = 0
        for start in startingNums:
            currNum = start
            currSeq += 1
            while currSeq != 0:
                if (currNum + 1) in uniqueNums:
                    currNum += 1
                    currSeq += 1
                else:
                    if currSeq > largestSeq:
                        largestSeq = currSeq

                    currNum = -1
                    currSeq = 0
        
        return largestSeq