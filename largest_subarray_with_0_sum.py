class Solution:
    """
    Given an array having both positive and negative integers.
    The task is to compute the length of the largest subarray with sum 0.

    Example 1:
    Input: N = 8
    A[] = {15,-2,2,-8,1,7,10,23}
    Output: 5
    Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.
    """
    def maxLen(self, n, arr):
        max_len = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += arr[j]
                if sum == 0:
                    max_len = max(max_len, j-i+1)
        return max_len 

N = 8
A = [15,-2,2,-8,1,7,10,23]   
solution = Solution()
solution.maxLen(N, A)
