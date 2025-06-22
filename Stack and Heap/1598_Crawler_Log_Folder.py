from collections import deque
import re
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ## TC: O(n), SC: O(n)
        operations = deque([])
        for log in logs:
            if len(operations) and log == "../":
                operations.pop()
            elif re.search("^[a-z0-9]*/", log):
                operations.append(log)
        
        return len(operations)