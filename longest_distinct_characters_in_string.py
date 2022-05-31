class Solution:
    """
    Given a string S, find the length of the longest
    substring with all distinct characters.
    
    Example:
    Input:
    S = "geeksforgeeks"
    Output: 7
    Explanation: "eksforg" is the longest 
    substring with all distinct characters.
    """
    def longestSubstrDistinctChars(self, S):
        max_len = 0
        for i in range(len(S)):
          k = 0
          while i+k < len(S):
            k += 1
            characters_list = [c for c in S[i:i+k]]
            characters_list.sort()
            unique_characters_list = list(set(characters_list))
            unique_characters_list.sort()
            if unique_characters_list == characters_list:
              max_len = max(max_len, len(set(characters_list)))
        return max_len
