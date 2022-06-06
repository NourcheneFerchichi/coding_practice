class Solution:
    def romanToDecimal(self, S): 
        """
        Given a string in roman no format (s)  your task is to convert it to an integer.
        Example:
        Input: S = XI
        Output:  11
        """
        result = 0
        i = 0
        rom_char = {}
        rom_char["I"] = 1
        rom_char["V"] = 5
        rom_char["X"] = 10
        rom_char["L"] = 50
        rom_char["C"] = 100
        rom_char["D"] = 500
        rom_char["M"] = 1000

        while i < len(S):
            if (i != len(S)-1 and rom_char[S[i]] < rom_char[S[i+1]]):
              result += rom_char[S[i+1]] - rom_char[S[i]]
              i += 2
              continue
            else:
              result += rom_char[S[i]]
            i += 1
        return result
        
S = "XI"
solution = Solution()
result = solution.romanToDecimal(S)
print(result)
