from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # If new interval comes before the current, then it also comes before all after current
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If new interval comes after the current, then we havent found the right spot yet
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if overlap, then update the new interval to be the intersection of current and newinterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res