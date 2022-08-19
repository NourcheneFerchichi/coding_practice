class Solution():
  def reverseInGroups(self, arr, N, K):
    """
    Given an array arr[] of positive integers of size N.
    Reverse every sub-array group of size K.

    Example 1:
    Input:
    N = 5, K = 3
    arr[] = {1,2,3,4,5}
    Output: 3 2 1 5 4
    Explanation: First group consists of elements 1, 2, 3.
    Second group consists of 4,5.
    """
    # initialize step
    i = 0
    while i<N:
      # initialize left and right indexes
      left = i
      right = min(i+K-1, N-1) # handle the case where right>N
      while left<right:
        # update left and right values
        arr[left], arr[right] = arr[right], arr[left]
        # update left and right indexes
        left += 1
        right -= 1
      # update step
      i += K
    return arr

N = 9
K = 3
arr = [1, 2, 3, 4, 5 , 6, 7, 8, 9]
solution = Solution()
solution.reverseInGroups(arr, N, K)
