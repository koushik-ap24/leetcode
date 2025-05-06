from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Use scanning
        if len(strs) == 1:
            return strs[0]
        
        longestPrefix = strs[0]
        for i in range(1, len(strs)):
            str_1 = strs[i]
            prefix = ""
            for j in range((min(len(str_1), len(longestPrefix)))):
                if str_1[j] == longestPrefix[j]:
                    prefix += longestPrefix[j]
                else:
                    break
            
            longestPrefix = prefix
        
        return longestPrefix


        ## Better solution, only compare first and last string after sorting list

        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 