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
