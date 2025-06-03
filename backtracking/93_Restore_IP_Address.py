from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ## MY approach - backtracking by keepint track of current number being formed
        res = []
        address = []

        def dfs(i, dotCount, currNum):
            # base case
            if i >= len(s):
                if dotCount == 3 and address[-1] != ".":
                    res.append(''.join(address))
                return
            
            
            if len(currNum) > 0 and ((currNum[0] == "0") or int(currNum + s[i]) > 255):
                return
   
            # Can only put down dot if dotcount < 3
            address.append(s[i])
            if dotCount < 3:
                address.append(".")
                dfs(i+1, dotCount+1, "")
                address.pop()
            
            
            dfs(i+1, dotCount, currNum + s[i])
            address.pop()
                

        dfs(0,0,"")
        return res

        ## Memory Optimsed version: (dont need to keep track of currNum)
        res = []

        def dfs(start: int, segments: List[str]):
            if len(segments) == 4:
                if start == len(s):
                    res.append('.'.join(segments))
                return

            for length in range(1, 4):  # segment lengths: 1 to 3
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                # Skip if segment has leading zeros or > 255
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

                dfs(start + length, segments + [segment])

        dfs(0, [])
        return res
        