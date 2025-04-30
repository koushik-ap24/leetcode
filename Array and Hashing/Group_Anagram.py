from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        hashmap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]

        result = []
        for key,value in hashmap.items():
            result.append(value)
        
        return result