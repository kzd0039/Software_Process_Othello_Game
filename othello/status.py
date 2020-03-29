"""
    Created to determine the status of the game
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    @Author: Kun Ding
"""

import math


def _status(parms):
    tokens = {'light': 1, 'dark': 2, 'blank': 0}

    
    ERROR01 = 'error: light/blank/dark/size non-integer'
    ERROR02 = 'error: light/blank/dark/size out of bounds'
    ERROR03 = 'error: light/blank/dark not unique'
    ERROR04 = 'error: missing board'
    ERROR05 = 'error: non-square board'
    ERROR06 = 'error: odd board'
    
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
    
    if 'board' not in parms:
        return {'status': ERROR04}
    
    board = parms['board']
    size = int(math.sqrt(len(board)))
    if size**2 != len(board):
        return {'status': ERROR05}
    if size%2 != 0:
        return {'status': ERROR06}
    
    
    return 















