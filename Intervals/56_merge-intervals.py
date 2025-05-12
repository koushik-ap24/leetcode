from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        res = []
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            # If new interval comes before the current, then it also comes before all after current
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            # if overlap, then update the new interval to be the intersection of current and newinterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res