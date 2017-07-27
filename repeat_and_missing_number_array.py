#You are given a read only array of n integers from 1 to n.
#
#Each integer appears exactly once except A which appears twice and B which is missing.
#
#Return A and B.
#
#Note: Your algorithm should have a linear runtime complexity.
#
#
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
       B = []
       repeat = -1
       missing = -1
       for i in range(0,len(A)):
           B.append(0)
       for i in range(0,len(A)):
           B[A[i]-1] += 1
           
       for i in range(0,len(B)):
           if B[i] == 2:
                repeat = i+1
           if B[i] == 0:
                missing = i+1
                
       return [repeat,missing] 
