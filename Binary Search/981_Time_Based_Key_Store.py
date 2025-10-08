from collections import defaultdict

class TimeMap:
    ## Key insight: Each call to set() is in increasing order!
    # So the array will be sorted by default for each key
    # TC: O(1) for set, O(logm) for get

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        searchSpace = self.store[key]
        res = ""
        left = 0
        right = len(searchSpace) - 1

        while left <= right:
            mid = (left + right) // 2
            if searchSpace[mid][0] <= timestamp:
                res = searchSpace[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res