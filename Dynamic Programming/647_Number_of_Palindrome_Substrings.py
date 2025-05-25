## Easiest way is to use two pointers, expand outwards approach for palindrome
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res