from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ## Brute Force Approach: Sliding Window + Hashing
        # TC: O(n), SC: O(n^2)
        subStringCount = defaultdict(int)
        maxCount = 0

        for size in range(minSize, maxSize + 1):
            seen = defaultdict(int)
            left = 0
            for right in range(len(s)):
                seen[s[right]] += 1
                if (right - left + 1) == size:
                    if len(seen) <= maxLetters:
                        subStringCount[s[left: right+1]] += 1
                        maxCount = max(maxCount, subStringCount[s[left: right+1]])
                    
                    seen[s[left]] -= 1
                    if seen[s[left]] == 0:
                        seen.pop(s[left])
                    left += 1
        
        return maxCount
        
        
        ## Optmised Approach: Hashtable + sliding window
        # TC: O(n), SC: O(n)
        # We only need to check substrings of size minSize, since larger sizes will contain the same substring of size minSize
        subStringCount = defaultdict(int)
        maxCount = 0
        left = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1
            if (right - left + 1) == minSize:
                if len(seen) <= maxLetters:
                    subStringCount[s[left: right+1]] += 1
                    maxCount = max(maxCount, subStringCount[s[left: right+1]])
                
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    seen.pop(s[left])
                left += 1
            
        
        return maxCount