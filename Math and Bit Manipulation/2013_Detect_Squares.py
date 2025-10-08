from collections import defaultdict
from typing import List


class DetectSquares:
    ## Approach: Use a hashmap to count occurrences of points
    ## TC: O(n) for add, O(m) for count, SC: O(n)
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.points.items():
            ## Check for square condition
            # The other point must form diagonal with (px, py) using the diagonal property
            # That is, the absolute difference in x and y coordinates must be equal
            # Also, x and y coordinates must be different to avoid line cases
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += cnt * self.points.get((px, y), 0) * self.points.get((x, py), 0)
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)