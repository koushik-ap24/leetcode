class Solution:
    def maxScore(self, s: str) -> int:
        # Initially consider the split as all numbers being part of right half, so count all ones.
        # Consider each point as a possible split. If the num is 0, then left score increases while right stays the same
        # If num is 1, left score stays the same while right score decreases by 1
        # The running max is the currMax or the score at the current split point.
        zero = 0
        one = s.count('1')
        res = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)

        return res