class Solution():
  """
  Given two arrays A and B of equal size N, the task is to find if given
  arrays are equal or not. Two arrays are said to be equal if both of
  them contain same set of elements, arrangements (or permutation) of
  elements may be different though.
  Note : If there are repetitions, then counts of repeated elements must also
  be same for two array to be equal.
  Example 1:
  Input:
  N = 5
  A[] = {1,2,5,4,0}
  B[] = {2,4,5,0,1}
  Output: 1
  Explanation: Both the array can be rearranged to {0,1,2,4,5}
  """
  def check(self, A, B, N):
    A.sort()
    B.sort()
    if A==B:
      return True
    else:
      return False
    
N = 5
A = [1,2,5,4,0]
B = [2,4,5,0,1]

solution = Solution()
solution.check(A, B, N)
