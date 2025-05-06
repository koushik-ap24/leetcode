from typing import List
from operator import itemgetter
import bisect

# Question: Warehouse array contains n warehouse each with capacity warehouse[i]. Catalog contains tuple elements, where catalog[i][0] is the capacity needed for that item, and catalog[i][1] is the required total capacity of all the other n-1 warehouses. The capacity of a warehouse can be upgraded by 1 unit by using 1 token. For each catalog item, find the minimum amount of tokens needed to satisfy the item requirements. Each catalog is treated independently, so return an array of ints where each element is the min token required for each catalog item.

class Solution:
    def minTokens(self, warehouse: List[int], catalog: List[List[int]]) -> str:
        # Set up prefix and suffix arrays
        n = len(warehouse)
        prefix = [0] * n
        suffix = [0] * n
        newArr = []
        newArr.append((warehouse[0], 0))
        result = []
        
        for i in range(1, n):
          prefix = prefix[i-1] + warehouse[i-1]
          newArr.append((warehouse[i], i))
          
        for j in range(n-1, -1, -1):
          suffix = suffix[j+1] + warehouse[j+1]
        
        # Sort array by warehouse capacity in ascending order
        newArr.sort(key=itemgetter(0))
        first_elements = [t[0] for t in newArr]

        for currCatalog in catalog:
          # Find largest warehouse <= currCatalog[0]
          idx = bisect.bisect_right(first_elements, currCatalog[0]) - 1
          warehouseTuple = ()
          if idx >= 0:
            warehouseTuple = newArr[idx]
          else:
            warehouseTuple = newArr[0]
          
          # Total tokens = increased capacity for chosen warehouse + backup storage.
          token = catalog[0] - warehouseTuple[0]
          backup_storage_diff = catalog[1] - prefix[warehouseTuple[1]] - suffix[warehouse[1]]
          if (backup_storage_diff) >= 0:
            token += backup_storage_diff
         
          result.append(token)
        
        return result