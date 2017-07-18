#You are in an infinite 2D grid where you can move in any of the 8 directions :
#
# (x,y) to 
#    (x+1, y), 
#    (x - 1, y), 
#    (x, y+1), 
#    (x, y-1), 
#    (x-1, y-1), 
#    (x+1,y+1), 
#    (x-1,y+1), 
#    (x+1,y-1) 
#
#You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
#
#Example :
#
#Input : [(0, 0), (1, 1), (1, 2)]
#Output : 2
#
class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
       steps = 0
       for i in range(0,len(X)):
           if i == len(X)-1 or len(X) == 1:
               break
           x_diff = abs(X[i+1] - X[i])
           y_diff = abs(Y[i+1] - Y[i])
           steps += max(x_diff,y_diff)
        
       return steps
