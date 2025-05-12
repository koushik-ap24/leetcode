from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals based on end time
        intervals.sort(key = lambda i : i[1])
        compliantIntervals = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # Only add the interval if it starts after the last complaint interval
            if (start >= compliantIntervals[-1][1]):
                compliantIntervals.append([start, end])
        
        # return diff between sets
        return abs(len(intervals)-len(compliantIntervals))

