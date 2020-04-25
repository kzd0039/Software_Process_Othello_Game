'''
    Created to place token on board
    Baselined: April 25, 2020
'''


import math
import collections
import hashlib

def _place(parms):
    tokens = {'light':1, 'dark':2, 'blank':0}
    if 'light' in parms:
        r = isValidTokens(parms['light'])
        if not isinstance(r, int):
            return r
        tokens['light'] = r
        
    if 'dark' in parms:
        r = isValidTokens(parms['dark'])
        if not isinstance(r, int):
            return r
        tokens['dark'] = r
        
    if 'blank' in parms:
        r = isValidTokens(parms['blank'])
        if not isinstance(r, int):
            return r
        tokens['blank'] = r
    
    light = str(tokens['light'])
    dark = str(tokens['dark'])
    blank = str(tokens['blank'])
    
    ERROR01 = 'error: light/blank/dark not unique'
    if light == dark or dark == blank or light == blank:
        return {'status': ERROR01}
    
    
    ERROR02 = 'error: missing board'
    if 'board' not in parms or parms['board'] == None:
        return {'status': ERROR02}
    
    board = isValidBoard(tokens, parms['board'])
    if not isinstance(board, list):
        return board
    
    size = int(math.sqrt(len(board)))
    
    
    ERROR03 = 'error: missing location'
    if 'location' not in parms or parms['location'] == None:
        return {'status': ERROR03}
    
    location = isValidLocation(parms['location'])
    if not isinstance(location, list):
        return location
    
    
    ERROR04 = 'error: missing integrity'
    if 'integrity' not in parms or parms['integrity'] == None:
        return {'status': ERROR04}
    
    token_to_place = isValidIntegrity(parms['integrity'], board, light, dark, blank)
    if not isinstance(token_to_place, str):
        return token_to_place
    
def isValidTokens(token):
    ERROR01 = 'error: light/blank/dark non-integer'
    ERROR02 = 'error: light/blank/dark out of bounds'
    try:
        int_token = int(token)
    except:
    #If value of 'light' is not integer, return corresponding error message
        return {'status': ERROR01}
    #If value of 'light' is not in range [0,9], return corresponding error message
    if int_token > 9 or int_token < 0:
        return {'status': ERROR02}
    
    return int_token


def isValidBoard(tokens, input_board):
    ERROR01 = 'error: invalid board'
    ERROR02 = 'error: non-square board'
    ERROR03 = 'error: board size out of bounds'
    ERROR04 = 'error: odd board'
    ERROR05 = 'error: board with non-light/dark/blank tokens'
    
    try:
        board = input_board[1:-1].split(',')
    except:
        return {'status': ERROR01}
    
    len_board = len(board)
    #Get square root of the length of board and convert it to integer
    size = int(math.sqrt(len_board))
    #If board is non-square, return corresponding error message
    if size**2 != len_board:   
        return {'status': ERROR02}
    
    if size < 6 or size > 16:
        return {'status': ERROR03}

    if size%2 != 0:
        return {'status': ERROR04}
    
    light = str(tokens['light'])
    dark = str(tokens['dark'])
    blank = str(tokens['blank'])
    
    count = collections.Counter(board)
    if count[light] + count[dark] + count[blank] != len_board:
        return {'status': ERROR05}
    
    return board
  

def isValidLocation(input_location):
    ERROR01 = 'error: invalid location'
    try:
        location =[int(x) for x in input_location.split(':')]
    except:
        return {'status': ERROR01}
    return location
    

def isValidIntegrity(input_integrity, board, light, dark, blank):
    ERROR01 = 'error: invalid integrity'
    ERROR02 = 'error: incorrect integrity'
    if len(input_integrity) != 64:
        return{'status': ERROR01}
        
    string1 = ''.join(board) + '/' + light +'/' +  dark +'/' +  blank + '/' +  light
    string2 = ''.join(board) + '/' + light + '/' + dark +'/' +  blank + '/' + dark 
    integrity1 = hashlib.sha256(string1.encode()).hexdigest()
    integrity2 = hashlib.sha256(string2.encode()).hexdigest()
    
    if input_integrity == integrity1:
        return 'light'
    if input_integrity == integrity2:
        return 'dark'
    return {'status': ERROR02}


def get_index(row, column, size):
    #check if the row is column is valid, return -1 if out of bounds, return index in the board if valid.
    if row >= 0 and row <size and column >= 0 and column < size:
        return row*size + column
    else:
        return -1















