from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        ## Approach: Brute Force + Hashset
        # Find all possible heights and widths by considering the fences
        # Then find the max common height and width
        # TC: O(m^2 + n^2), SC: O(m + n)
        def getCandidates(fences, l):
            fences.append(1)
            fences.append(l)

            fences.sort()

            candidates = set()
            for i in range(len(fences)):
                for j in range(i+1, len(fences)):
                    candidates.add(fences[j]-fences[i])
            
            return candidates
        
        heights = getCandidates(hFences, m)
        widths = getCandidates(vFences, n)
        common = heights.intersection(widths)

        if len(common):
            size = max(common)
            return (size * size) % (10 ** 9 + 7)
        
        return -1