from typing import List

# Question: given 2 number arrays, where they are permutations of each other, find the largest common subsequence between them and figure out how many nums (processes) are in the wrong order.
# e.g. - correctSequence = [2,3,5,1,4]
#          sequence = [5,2,3,4,1]
# So LCS is 2,3,1. Here 5 is incorrect since it depends on 3, but occurs before 3. 4 is also incorrect since it depends on 1, but occurs before it

# Another example:
# correctSequence = [4,2,3,5,1,6]
# sequence = [2,3,5,1,6,4]
# Here even though only one element (4) is out of order the number of incorrect processes is 5 since all the other ones depend on it, but occur before it in the transpired sequence

# This question requires that for each process, we track all its dependencies (processes that should come before it). Then we check if any process appears before its dependencies in the actual sequence. This gives us the exact count of processes that are in the wrong order

# Implements a binary indexed tree
class Solution:
    def findMisalignedProcesses(self, correct_sequence: List[int], sequence: List[int]) -> str:
      # Create a rank map from the correct sequence
      rank = {num: i for i, num in enumerate(correct_sequence)}
      
      # Convert the actual sequence to ranks
      rank_sequence = [rank[num] for num in sequence]
      
      n = len(correct_sequence)
      wrong_processes = set()
      
      # Binary Indexed Tree (bit)
      bit = [0] * (n + 1)
      
      def update(idx, val):
          while idx <= n:
              bit[idx] += val
              idx += idx & -idx
      
      def query(idx):
          result = 0
          while idx > 0:
              result += bit[idx]
              idx -= idx & -idx
          return result
      
      # Process the sequence from right to left
      for i in range(n-1, -1, -1):
          process_rank = rank_sequence[i]
          
          # Count elements with smaller ranks we've seen after this element
          smaller_seen_after = query(process_rank)
          
          if smaller_seen_after > 0:
              wrong_processes.add(sequence[i])
          
          # Mark this rank as seen
          update(process_rank + 1, 1)
      
      return len(wrong_processes)