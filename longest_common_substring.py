class Solution:
		"""
		Given two strings. The task is to find the length of the longest common substring.
		Example:
		Input: S1 = "ABCDGH", S2 = "ACDGHR"
		Output: 4
		Explanation: The longest common substring is "CDGH" which has length 4.
		"""
		def longestCommonSubstr(self, S1, S2, n, m):
			longest_com = 0
			for i in range(n):
				for j in range(m):
					k = 0
					while ((i + k) < n and (j + k) < m 
        				and S1[i + k] == S2[j + k]): 
						k = k + 1
						longest_com = max(longest_com, k)
			return longest_com

solution = Solution()
S1 = "ABCDGH"
S2 = "ACDGHR"
result = solution.longestCommonSubstr(S1, S2, len(S1), len(S2))
print(result)
