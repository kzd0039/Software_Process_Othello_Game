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
    
    light = tokens['light']
    dark = tokens['dark']
    blank = tokens['blank'] 
    
    ERROR01 = 'error: light/blank/dark not unique'
    if light == dark or dark == blank or light == blank:
        return {'status': ERROR01}
    
    
    ERROR02 = 'error: missing board'
    if 'board' not in parms or parms['board'] == None:
        return {'status': ERROR02}
    
    board = isValidBoard(tokens, parms['board'])
    if not isinstance(board, list):
        return board
    
    
    
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
  




















