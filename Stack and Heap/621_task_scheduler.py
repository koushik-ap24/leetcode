from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    # Add task with updated count (currCount - 1) to the queue, where it will stay until time + n
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                # At this point the task at the front of the queue is ready again for consideration in the next iteration, so we add it now
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        
