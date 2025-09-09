from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Approach: Interval overlap greedy
        # Sort intervals by end time, then iterate through intervals
        # If the start of the current interval is greater than the end of the last interval, we need a new arrow
        # TC: O(n log n), SC: O(1)
        
        points.sort(key=lambda x: x[1])

        arrows = 1
        candidatePoint = points[0][1]
        for balloon in points:
            if balloon[0] > candidatePoint:
                candidatePoint = balloon[1]
                arrows += 1
        
        return arrows