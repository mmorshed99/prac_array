#Given a non-negative number represented as an array of digits,
#
#add 1 to the number ( increment the number represented by the digits ).
#
#The digits are stored such that the most significant digit is at the head of the list.
#
#Example:
#
#If the vector has [1, 2, 3]
#
#the returned vector should be [1, 2, 4]
#
#as 123 + 1 = 124.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
       B = []
       C = []
       tag_0 = 0
       for i in range(0,len(A)):
           if A[i] == 0 and tag_0 ==0:
               if A[-1] == 0:
                   B.append(1)
               continue
           else:
               tag_0 = 1
           B.append(A[i])
           if i == len(A) - 1:
               B[-1] += 1
               if B[-1] == 10:
                   count = 2
                   B[-1] = 0
                   j = len(B) - 2
                   while (count < (len(B) + 1)):
                       count += 1
                       B[j] = B[j] + 1
                       if B[j] != 10:
                           break
                       
                       B[j] = 0
                       j = j -1
                   if B[0] == 10:
                       B[0] = 0
                   if B[0] == 0:
                       B.insert(0,1)
       return B               
