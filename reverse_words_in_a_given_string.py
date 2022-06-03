class Solution:
    """
    Given a String S, reverse the string without reversing its individual words.
    Words are separated by dots.
    Example:
    Input: S = i.like.this.program.very.much
    Output: much.very.program.this.like.i
    Explanation: Reversing the whole string(not individual words)
    """
    def reverseWords(self,S):
        result = ""
        word_list = S.split(".")
        for i in range(len(word_list)-1, -1, -1):
            result += word_list[i]
            result += "."
        return result[:-1]

      
S = "i.like.this.program.very.much"
solution = Solution()
result = solution.reverseWords(S)
print(result)
