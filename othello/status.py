"""
    Created to determine the status of the game
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    Modified: Mar 29, 2020
    Modified: Mar 30, 2020
    @Author: Kun Ding
"""

import math
import collections
import hashlib



def _status(parms):
    #Create a dictionary to store the value of three tokens and set the default value respectively
    tokens = {'light': 1, 'dark': 2, 'blank': 0}

    #Define the proper error message
    ERROR01 = 'error: light/blank/dark non-integer'
    ERROR02 = 'error: light/blank/dark out of bounds'
    ERROR03 = 'error: light/blank/dark not unique'
    ERROR04 = 'error: missing board'
    ERROR05 = 'error: non-square board'
    ERROR06 = 'error: odd board'
    ERROR07 = 'error: board with non-light/dark/blank tokens'
    ERROR08 = 'error: missing integrity'
    ERROR09 = 'error: invalid integrity'
    ERROR10 = 'error: board size out of bounds'
    ERROR11 = 'error: short integrity'
    ERROR12 = 'error: long integrity'
    
    #Validate input
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
    
    
    #If 'board' is missing or the value of it is None, return corresponding error message
    if 'board' not in parms or parms['board'] == None:
        return {'status': ERROR04}
    board = parms['board']
    len_board = len(board)
    #Get square root of the length of board and convert it to integer
    size = int(math.sqrt(len_board))
    #If board is non-square, return corresponding error message
    if size**2 != len_board:   
        return {'status': ERROR05}
    #If board size out of bounds, return corresponding error message
    if size < 6 or size > 16:
        return {'status': ERROR10}
    #If board size not even, return corresponding error message
    if size%2 != 0:
        return {'status': ERROR06}
    count = collections.Counter(board)
    #If count contains keys other than light/dark/blank, return corresponding error message.
    if set(count.keys()) != set([light, dark, blank]):
        return {'status': ERROR07}
    
    
    
    #If missing 'integrity' or it's value is None, return corresponding error message
    if 'integrity' not in parms or parms['integrity'] == None:
        return {'status': ERROR08}
    integrity = parms['integrity']
    #If length of integrity is shorter than 64, return corresponding error message
    if len(integrity) < 64:
        return {'status': ERROR11}
    #If length of integrity is greater than 64, return corresponding error message
    if len(integrity) > 64:
        return {'status': ERROR12}
  
    #If blank, dark or light is not unique, return corresponding error message
    if light == dark or light == blank or dark == blank:
        return {'status': ERROR03}
    
    #Construct the string for calculation of 'integrity', one end with <dark>, another end with <light>
    string = ''.join(str(x) for x in board) 
    string1 = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
    string2 = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(light)
    #Calculate the 'integrity' 
    integrity1 = hashlib.sha256(string1.encode()).hexdigest()
    integrity2 = hashlib.sha256(string2.encode()).hexdigest()
    #if the input 'integrity' doesn't match the two, return corresponding error messages.
    if not(integrity1 == parms['integrity'] or integrity2 ==  parms['integrity']):
        return {'status': ERROR09}
    
    #Create a list to store eight directions, down, up, right, left, down-left, down-right, up-left, up-right 
    Directions = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1]]
    #Create dictionary to store the number of light and dark that could be placed on board
    result = {light:0, dark:0}
    
    
    #Scan the board. i is the row number, j is the column number.
    for i in range(size):
        for j in range(size):
            #Get the current index based on the row, column and size of the board.
            index = get_index(i,j,size)
            #If the token is blank, means it is possible to place a light or dark.
            if board[index] == blank:
                #From this token, check eight directions one by one.
                for direction in Directions:
                    #Create list to keep track of tokens as it moves.
                    stack = [ ]
                    #If is_valid() return the token that is dark or light, update the number in result.
                    key = is_valid(i,j,size,board,tokens,stack,direction)
                    if key in result:
                        result[key] += 1
    
    #if both value are greater than 0, next_token can be light or dark
    if result[light] > 0 and result[dark] > 0:
        return {'status': 'ok'}
    #If only  light is greater than 0, next_token can only be light
    if result[light] > 0:
        return {'status': 'light'}
    #If only  dark is greater than 0, next_token can only be dark
    if result[dark] > 0:
        return {'status': 'dark'}
    #If neither the dark and light could be placed, the game is end
    return {'status': 'end'}
    
def get_index(row, column, size):
    #check if the row is column is valid, return -1 if out of bounds, return index in the board if valid.
    if row >= 0 and row <size and column >= 0 and column < size:
        return row*size + column
    else:
        return -1


def is_valid(row, column, size, board, tokens, stack, direction):
    #Move forward according to the direction
    row += direction[0]
    column += direction[1]
    #if index is out of bounds, return -1 to show current path is invalid
    i = get_index(row, column, size)
    if i == -1:
        return -1
    
    current = board[i]
    #If current token is blank, return -1 to show current path is invalid
    if current == tokens['blank']:
        return -1
    #If the current token is not the same with previous, return current token to show that this token can place on the original blank token
    if stack and current != stack[-1]:
        return current
    else:
        #If the current is the same with previous, store the current token and keep moving
        stack.append(current)
        return is_valid(row, column, size, board, tokens, stack, direction)
   
    






