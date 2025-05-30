from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Constraints:
        # s1 and s2 will not be empty
        # s1 and s2 will only contain alphanumeric characters
        # all characters will be lowercase only

        # Approach:
        # Create a character count hashMap for s1 and s2 window
        s1Map = Counter(s1)
        windowMap = defaultdict(int)

        # Iterate through s2 in linear order
        left = 0
        for right in range(len(s2)):
        # Maintain a sliding window of size m = len(s1)
        # Maintain count of characters in the window
            windowMap[s2[right]] += 1
        # If the count is the same as s1, return True
            if (right - left + 1) == len(s1):
                if windowMap == s1Map:
                    return True
                windowMap[s2[left]] -= 1
                if windowMap[s2[left]] == 0:
                    windowMap.pop(s2[left])
                left += 1
        
        # At the end of iteration, return False
        return False

        # TC: O(n), SC: O(1) (because both hashmaps can only have at most 26 key-value pairs!)
