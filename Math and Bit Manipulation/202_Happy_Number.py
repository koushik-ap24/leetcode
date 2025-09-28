class Solution:
    def isHappy(self, n: int) -> bool:
      ## Approach: HashSet to detect cycles
      # Intuition: We can use a set to keep track of the numbers we have seen so far.
      # If we see a number again, it means we are in a cycle and will never reach 1.
      # If we reach 1, we return True.
      ## TC: O(log n), SC: O(log n)
      seen = set()
      num = n

      while num not in seen:
          if num == 1:
              return True
          
          seen.add(num)
          digits = str(num)
          num = 0
          for i in digits:
              num += int(i) ** 2

      return False