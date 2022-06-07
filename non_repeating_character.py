from collections import Counter

class Solution:
    """
    Return the first non-repeating character in S.
    If there is no non-repeating character, return '$'.
    Example:
    Input: zxvczbtxyzvy
    Output: c
    """
    def nonrepeatingCharacter(self, s: str) -> str:
        char_counts = Counter(s)
        the_char = "$"
        
        for char in s:
            occurence = char_counts[char]
            if occurence == 1:
                the_char = char
                break
        return the_char

S = "zxvczbtxyzvy"
solution = Solution()
result = solution.nonrepeatingCharacter(S)
print(result)
