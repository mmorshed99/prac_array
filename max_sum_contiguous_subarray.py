#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
#For example:
#
#Given the array [-2,1,-3,4,-1,2,1,-5,4],
#
#the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
#For this problem, return the maximum sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
       max_current = A[0]
       max_global = A[0]
       if len(A)>1:
           for i in range(1, len(A)):
               max_current = max(A[i], max_current+A[i])
               if max_current > max_global:
                   max_global = max_current
       return max_global
#
#
#
# Used Kadane's algorithm       
