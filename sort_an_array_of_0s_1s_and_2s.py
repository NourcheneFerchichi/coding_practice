class Solution:
    """
    Given an array of size N containing only 0s, 1s, and 2s;
    sort the array in ascending order.
    Example:
    Input: N = 5, arr[]= {0 2 1 2 0}
    Output: 0 0 1 2 2
    Explanation: 0s 1s and 2s are segregated into ascending order.
    """
    def sort012(self,arr,n):
        count_0 = arr.count(0)
        count_1 = arr.count(1)
        i = 0
        while i<count_0:
            arr[i] = 0
            i += 1
        while i<count_0+count_1:
            arr[i] = 1
            i += 1
        while i<len(arr):
            arr[i] = 2
            i += 1
        return arr

arr = [0, 2, 1, 2, 0, 0]
solution = Solution()
solution.sort012(arr, len(arr))
