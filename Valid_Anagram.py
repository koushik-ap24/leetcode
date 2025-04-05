class Solution:
    # TC = O(mlog(m) + nlog(n))
    # SC = O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_s != sorted_t:
            return False
        
        return True
    
    # Best Solution = use Hash Map!
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        