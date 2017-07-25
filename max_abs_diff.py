#You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
#f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
#
#
#A=[1, 3, -1]
#
#f(1, 1) = f(2, 2) = f(3, 3) = 0
#f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
#f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
#f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
#
#So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
       max1 = -9999999999
       max2 = -9999999999
       max3 = -9999999999
       max4 = -9999999999
       max =  -9999999999
       def findmax(a,b):
           if a>b:
               return a
           else: 
               return b
    
       for i in range(0,len(A)):
           max1 = findmax(max1,A[i]+i)
           max=findmax(max,max1-A[i]-i)
           max2 = findmax(max2,-A[i]+i)
           max=findmax(max,max2+A[i]-i)
           max3 = findmax(max3,A[i]-i)
           max=findmax(max,max3-A[i]+i)
           max4 = findmax(max4,-A[i]-i)
           max=findmax(max,max4+A[i]+i)
       return max
