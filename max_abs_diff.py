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
