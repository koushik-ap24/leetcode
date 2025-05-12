import heapq
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    ## Optimal solution - Min Heap
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        # Min heap keeps track of the ending times of the rooms we need to use
        min_heap = [intervals[0]]

        for interval in intervals[1:]:
            # If meeting starts after the earliest ending meeting, reuse that same room and update its ending time
            # Otherwise, add a new room and update its end time.
            if min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

    ## My solution
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda pair:pair.end)
        days = []

        for interval in intervals:
            insertDay = 0
            for i in range(len(days)):
                if interval.start >= days[i][-1].end:
                    break
                insertDay += 1
            if insertDay < len(days):
                days[insertDay].append(interval)
            else:
                days.append([interval])
        
        return len(days)