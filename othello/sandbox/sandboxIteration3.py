'''
    Created to 
    Baselined: April 25, 2020
'''
import collections

print(isinstance(2, int))

print(''[1:-1].split(','))

board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
         
         
board = board[1:-1].split(',')
count = collections.Counter(board)
print(count)