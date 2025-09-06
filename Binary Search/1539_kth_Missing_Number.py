from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # maintain a counter of expected items
        # linear scan
        # TC: O(n), SC: O(1)

        # num = 1
        # for i in range(len(arr)):
        #     if num != arr[i]:
        #         while num < arr[i]:
        #             k -= 1
        #             if k == 0:
        #                 return num
        #             num += 1
            
        #     num = arr[i] + 1
        
        # while k != 1:
        #     num += 1
        #     k -= 1
        
        # return num

        ## Binary search method
        left = 0
        right = len(arr) - 1
        idx = 0
        while left <= right:
            mid = (left + right) // 2
            idx = mid
            expected = mid + 1
            if arr[mid] - expected < k:
                # look right
                left = mid + 1
            else:
                right = mid - 1
        
        # print(arr[idx])
        # if arr[idx] - (idx + 1) < k:
        #     return arr[idx] + k
        
        # if idx == 0:
        #     return k
        
        # missing = arr[idx-1] - (idx)
        # print(missing)
        # return arr[idx-1] + (k - missing)

        print(right)
        return right + k + 1
        

