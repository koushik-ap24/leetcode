import bisect


class HitCounter:

    # [(0,0),(1,1),(2,2),(3,3),(300,4)]
    ## Approach: Binary Search + Prefix Sum
    # Maintain a list of tuples where each tuple contains a timestamp and the cumulative hit count up to that timestamp.
    # Use binary search to find the range of timestamps that fall within the last 5 minutes.
    # TC: O(log n), SC: O(n)
    def __init__(self):
        self.hitCount = [(0,0)] # (timestamp, hitcount)

    def hit(self, timestamp: int) -> None:
        if timestamp == self.hitCount[-1][0]:
            self.hitCount[-1] = (timestamp, self.hitCount[-1][1] + 1)
        else:
            self.hitCount.append((timestamp, self.hitCount[-1][1] + 1))

    def getHits(self, timestamp: int) -> int:
        right = bisect.bisect_right(self.hitCount, timestamp, key=lambda x: x[0]) - 1
        left = bisect.bisect_right(self.hitCount, max(0, (timestamp - 300)), key=lambda x: x[0]) - 1
        return self.hitCount[right][1] - self.hitCount[left][1]