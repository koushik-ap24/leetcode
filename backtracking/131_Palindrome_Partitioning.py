from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # len(s) >= 1
        # s can be a substring of itself
        # s will only contain lowercase characters

        # abba
        # [['a','b','b','a'], ['abba']]

        # for each element, choose to either partition or not partition
        # if we choose to partition, then we check if the substring between the last partition and this is a palindrome
        # if true, then consider a valid parition and look at the rest of the string
        def isPalindrome(start, end):
            left = start
            right = end

            while left <= right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        res = []
        partition = []
        def dfs(i):
            if i == len(s):
                res.append(partition.copy())
                return

            for idx in range(i, len(s)):
                # Choose to partition if this substring is a palindrome, otherwise dont partition
                if isPalindrome(i, idx):
                    partition.append(s[i: idx+1])
                    dfs(idx+1)
                    # This pop automatically reverts the parition anyway, so no need for extra dfs call
                    partition.pop()
                
        
        dfs(0)
        return res
