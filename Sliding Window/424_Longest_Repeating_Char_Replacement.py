class Solution:
    # Key concept is you always want to replace chars with the max frequency char in the window to reduce replacements
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            # Check if window is valid
            # number of replacements in current window = length - count of most frequent character in the window
            while (right - left + 1) - max(count.values()) > k:
                # decrease window size
                count[s[left]] -= 1
                left += 1
            
            # Once/If the window is valid, check if its the max size so far
            res = max(res, (right-left + 1))
        
        return res