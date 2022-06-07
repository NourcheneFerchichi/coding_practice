class Solution:
  """
  Given a string S, check if it is palindrome or not.
  Example:
  Input: S = "abba"
  Output: 1
  Explanation: S is a reverse S and S are the same
  """
  def isPalindrome(self, S:str) -> int:
    reverse_S = S[: : -1]
    if S == reverse_S:
        return 1
    else:
        return 0

S = "abba"
solution = Solution()
solution.isPalindrome(S)
