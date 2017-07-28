#You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.
#
#Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
#
#Notes: 
#- Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
#
#For example,
#S = 010
#Pair of [L, R] | Final string
#_______________|_____________
#[1 1]          | 110
#[1 2]          | 100
#[1 3]          | 101
#[2 2]          | 000
#[2 3]          | 001
#We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
#
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
     def maxSubArray(A):
       max_current = A[0]
       max_global = A[0]
       start_id_glob = 0
       end_id_glob = 0
       start_id_curr = 0
       end_id_curr = 0
       if len(A)>1:
           for i in range(1, len(A)):
               max_current_old = max_current
               max_current = max(A[i], max_current+A[i])
               end_id_curr = i
               if A[i] >  max_current_old+A[i]:
                 start_id_curr = i
               if max_current > max_global:
                   max_global = max_current
                   start_id_glob = start_id_curr
                   end_id_glob = end_id_curr
       return max_global,start_id_glob,end_id_glob

     list_S = list(A)
     new_S = []
     count_one = 0
     returned_val = 0
     for i in range(0,len(list_S)):
      list_S[i] = int(list_S[i])
      if list_S[i] == 0:
        new_S.append(1)
      else:
        new_S.append(-1)
        count_one += 1
     value, start, end = maxSubArray(new_S)
     for i in range(start,end+1):
        list_S[i] = 1
     for i in range(0,len(list_S)):
       if list_S[i] == 1:
        returned_val += 1
     if returned_val > count_one:
        return [start+1, end+1]
     else:
        return []
