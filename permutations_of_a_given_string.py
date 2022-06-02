import itertools

class Solution:
  """
  Given a string S: The task is to print all permutations of a given
  string in lexicographically sorted order.
  Example:
  Input: ABC
  Output: ABC ACB BAC BCA CAB CBA
  """
  def find_permutation(self, S: str) -> list:
      permutations = []
      characters = []
      
      # Extract all characters in S
      for char in S:
          characters += char
          
      # Create all possible character permutations
      permuted_characters = list(set(itertools.permutations(characters)))
      
      # Create permuted strings
      for p in permuted_characters:
          permutations.append("".join(p))
          
      # Sort permuted strings lexicographically
      permutations.sort()
      
      return permutations


S = "ABC"
solution = Solution()
permutations = solution.find_permutation(S)
print(permutations)
