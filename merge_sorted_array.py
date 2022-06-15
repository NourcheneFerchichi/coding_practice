from typing import List

class Solution(object):
    """
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and
    nums2 respectively: Merge nums1 and nums2 into a single array sorted in
    non-decreasing order.

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined
    elements coming from nums1.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Args:
        nums1 (List[int]): First array sorted in a non-decreasing order.
        m (int): Length of the first array
        nums2 (List[int]): Second array sorted in a non-decreasing order.
        n (int): Length of the second array.

        Returns:
        nums1 (List[int]):  The result of the merge.
        """
        while m>0 and n>0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n>0:
            nums1[:n] = nums2[:n]
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
