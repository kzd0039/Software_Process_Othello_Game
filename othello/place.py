'''
    Created to place token on board
    Baselined: April 25, 2020
'''




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
    if light == dark or dark == blank or dark == blank:
        return {'status': ERROR01}
    
    ERROR02 = 'error: missing board'
    if 'board' not in parms:
        return {'status': ERROR02}

    ERROR02 = 'error: invalid board'
    
    
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


def isValidBoard(tokens, board):
    pass
