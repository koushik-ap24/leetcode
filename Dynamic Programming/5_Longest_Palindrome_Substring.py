## Easiest way is to use two pointers, expand outwards approach for palindrome
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resIdxEnd = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r - l - 1) > resLen:
                resIdx = l+1
                resIdxEnd = r
                resLen = r - l - 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if (r - l - 1) > resLen:
                resIdx = l + 1
                resIdxEnd = r
                resLen = r - l - 1

        return s[resIdx : resIdxEnd]