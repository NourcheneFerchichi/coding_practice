class Solution:
    """
    Given a string S, find the longest palindromic substring in S.
    Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S).
    Palindrome string: A string which reads the same backwards.
    More formally, S is palindrome if reverse(S) = S.
    Example:
    Input:  S = "aaaabbaa"
    Output: "aabbaa"
    Explanation: The longest Palindromic substring is "aabbaa".
    """
    def checkPalin(self, S:str, l:int, r:int) -> str:
        """
        Given a string S, returns substrings in S
        that are palindrom.
        """
        while l>=0 and r<len(S) and S[l]==S[r]:
            l-=1
            r+=1
        return S[l+1:r]
        
    def longestPalin(self, S:str) -> str:
        """
        Retruns the longest palindrom.
        """
        longest_palin = ""
        
        for i in range(len(S)):
            odd_palin = self.checkPalin(S, i, i)
            even_palin = self.checkPalin(S, i, i+1)
            
            if len(odd_palin)>len(even_palin):
                longest_even_odd = odd_palin
            else:
                longest_even_odd = even_palin
            
            if len(longest_even_odd)>len(longest_palin):
                longest_palin = longest_even_odd
                
        return longest_palin

S = "aaaabbaa"
solution = Solution()
palin = solution.longestPalin(S)
print("The longest palindrom in %s is %s" %(S,palin))
