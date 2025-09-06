from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Approach: Sliding window + hashmap
        # Turn into sliding window by instroducing hard upper limit (unique chars)
        # For each window without t unique chars, check the validity condition
        # If true, consider this substring as a candidate
        # If more than t unique chars, reduce window size until back to valid window
        # TC: O(26*n), SC: O(1) since hashmap size is capped at 26
        res = 0
        maxUnique = len(s) // k
        for i in range(1, maxUnique+1):
            left = 0
            unique = 0
            countAtLeastK = 0
            # Keep track of char counts in current window
            count = defaultdict(int)
            for right in range(len(s)):
                if s[right] not in count:
                    unique += 1
                count[s[right]] += 1

                if count[s[right]] == k:
                    countAtLeastK += 1
                
                # Window is valid if all distinct chars repeat at least k times in the window
                if unique == countAtLeastK:
                    res = max(res, (right - left) + 1)

                # If there are more than i unique chars, shrink window from left until back to i unique chars
                while unique > i:
                    # Update count of chars going below k repetitions.
                    if count[s[left]] == k:
                        countAtLeastK -= 1
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        count.pop(s[left])
                        unique -= 1
                    
                    left += 1
        
        return res