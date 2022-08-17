class Solution:
    def MissingNumber(self,array,n):
        array.sort()
        if array[0]!=1:
            return 1
        if array[n-2]!=n:
            return n
        for i in range(n-2):
            if array[i]+1 != array[i+1]:
                return array[i]+1
              
              
N = 10
A = [6,1,2,8,3,4,7,10,5]   
solution = Solution()
solution.MissingNumber(A, N)
