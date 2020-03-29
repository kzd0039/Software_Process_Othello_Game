"""
    Created to determine the status of the game
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    @Author: Kun Ding
"""

import math
import collections
import hashlib



def _status(parms):
    tokens = {'light': 1, 'dark': 2, 'blank': 0}

    
    ERROR01 = 'error: light/blank/dark/size non-integer'
    ERROR02 = 'error: light/blank/dark/size out of bounds'
    ERROR03 = 'error: light/blank/dark not unique'
    ERROR04 = 'error: missing board'
    ERROR05 = 'error: non-square board'
    ERROR06 = 'error: odd board'
    ERROR07 = 'error: board with non-light/dark/blank tokens'
    ERROR08 = 'error: missing integrity'
    ERROR09 = 'error: invalid integrity'
    
    if 'light' in parms:
        try:
            light = int(parms['light'])
        except:
        #If value of 'light' is not integer, return corresponding error message
            return {'status': ERROR01}
        #If value of 'light' is not in range [0,9], return corresponding error message
        if light > 9 or light < 0:
            return {'status': ERROR02}
        #Overwrite the value of 'light'
        tokens['light'] = light
        
    if 'dark' in parms:
        try:
            dark = int(parms['dark'])
        except:
        #If value of 'dark' is not integer, return corresponding error message
            return {'status': ERROR01}
        if dark > 9 or dark < 0:
            return {'status': ERROR02}
        #overwrite the value of dark
        tokens['dark'] = dark
        
    if 'blank' in parms:
        try:
            blank = int(parms['blank'])
        except:
        #If value of 'blank' is not integer, return corresponding error message
            return {'status': ERROR01}   
        if blank > 9 or blank < 0:
            return {'status': ERROR02}
        #overwrite the value of blank
        tokens['blank'] = blank
        
    light = tokens['light']
    dark = tokens['dark']
    blank = tokens['blank']   
    #If blank, dark or light is not unique, return corresponding error message
    if light == dark or light == blank or dark == blank:
        return {'status': ERROR03}
    
    if 'board' not in parms or parms['board'] == None:
        return {'status': ERROR04}
    
    board = parms['board']
    len_board = len(board)
    size = int(math.sqrt(len_board))
    if size**2 != len_board:
        return {'status': ERROR05}
    if size%2 != 0:
        return {'status': ERROR06}
    count = collections.Counter(board)
    if count[light] + count[dark] + count[blank] != len_board:
        return {'status': ERROR07}
    
    
    if 'integrity' not in parms or parms['integrity'] == None:
        return {'status': ERROR08}
    
    string = ''.join(str(x) for x in board) 
    string1 = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
    string2 = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(light)
    #Calculate the 'integrity' 
    integrity1 = hashlib.sha256(string1.encode()).hexdigest()
    integrity2 = hashlib.sha256(string2.encode()).hexdigest()
    
    if not(integrity1 == parms['integrity'] or integrity2 ==  parms['integrity']):
        return {'status': ERROR09}
    
    Directions = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1]]
    result = {light:0,dark:0}
    
    
    for i in range(size):
        for j in range(size):
            index = get_index(i,j,size)
            if board[index] == blank:
                for direction in Directions:
                    stack = [ ]
                    key = is_valid(i,j,size,board,tokens,stack,direction)
                    if key in result:
                        result[key] += 1
    
    if result[light] > 0 and result[dark] > 0:
        return {'status':'ok'}
    if result[light] > 0:
        return {'status': 'light'}
    if result[dark] > 0:
        return {'status': 'dark'}
    
    return {'status': 'end'}
    
def get_index(row, column, size):
    if row > 0 and row <size and column >= 0 and column < size:
        return row*size + column
    else:
        return -1


def is_valid(row, column, size, board, tokens, stack, direction):
    row += direction[0]
    column += direction[1]
    i = get_index(row, column, size)
    if i == -1:
        return -1
    current = board[i]
    
    if current == tokens['blank']:
        return -1
    
    if stack and current != stack[-1]:
        return current
    else:
        stack.append(current)
        return is_valid(row, column, size, board, tokens, stack, direction)
   
    






