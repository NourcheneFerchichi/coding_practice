class Solution:
    """
    Given two numbers as strings s1 and s2. Calculate their Product.
    Note: The numbers can be negative.
    Example :
    Input:
    s1 = "22"
    s2 = "-5"
    Output: -110
    """
    def returnNumber(self,s):
        resultat = 0
        if s[0] == "-":
            for i in range(1, len(s)):
                if s[i] in "0123456789":
                    resultat = resultat*10 + ord(s[i]) - ord("0")
                else:
                    return -1
            resultat *= -1
        else:
            for i in range(len(s)):
                if s[i] in "0123456789":
                    resultat = resultat*10 + ord(s[i]) - ord("0")
                else:
                    return -1
        return resultat

    def multiplyStrings(self,s1,s2):
        num_s1 = self.returnNumber(s1)
        num_s2 = self.returnNumber(s2)
        return num_s1 * num_s2

s1 = "22"
s2 = "-5"
solution = Solution()
result = solution.multiplyStrings(s1, s2)
print(result)
