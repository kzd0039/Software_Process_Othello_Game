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
    string = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
    #Calculate the 'integrity' 
    integrity = hashlib.sha256(string.encode()).hexdigest()
    
    if integrity != parms['integrity']:
        return {'status': ERROR09}
    
    
    
    
    
    
    
def index(row, column, size):
    return row*size + column










