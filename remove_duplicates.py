class Solution:
  """
  Given a string without spaces, the task is to remove duplicates from it.
  Note: The original order of characters must be kept the same.
  Example:
  Input: S = "gfg"
  Output: gf
  Explanation: Only keep the first occurrence
  """
  def removeDups(self, S:str) -> str:
    result = ""
    for char in S:
        if char not in result:
            result += char
    return result

S = "gfg"
solution = Solution()
result = solution.removeDups(S)
print(result)
