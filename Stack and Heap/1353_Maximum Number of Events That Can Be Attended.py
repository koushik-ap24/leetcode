import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Assumptions:
        # At least one event is given
        # Every event has a start and end day, where start <= end
        # Allowed to only attend one event a day
        # Event must start at the start of a day and end at the end of a day (integer numbers)
        # No need to attend an event for its entirety, must only attend for a whole number of days

        ## Approach: Min-Heap + Greedy
        ## Intuition: We want to attend the event that ends the soonest first on each day
        # TC: O(nlogn), SC: O(n)
        events.sort(key=lambda x: (x[0],x[1]))
        min_heap = []  # A min-heap to store the end days of available events
        res = 0
        event_idx = 0
        num_events = len(events)
        
        # We can stop checking days once we've processed all events and the heap is empty.
        # Let's find the last possible day an event can occur.
        max_day = 0
        for start, end in events:
            max_day = max(max_day, end)

        # Iterate through each day
        for day in range(1, max_day + 1):
            # 1. Add all events that start today to the min_heap
            while event_idx < num_events and events[event_idx][0] == day:
                end_day = events[event_idx][1]
                heapq.heappush(min_heap, end_day)
                event_idx += 1

            # 2. Remove all events from the heap that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # 3. If there are available events, attend the one that ends the soonest
            if min_heap:
                # attend the most urgent event
                heapq.heappop(min_heap)
                res += 1
                
        return res