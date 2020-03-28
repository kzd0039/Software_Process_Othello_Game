"""
    Created to determine the status of the game
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    @Author: Kun Ding
"""
def _status(parms):
    result = {}
    result['tokens'] = {'light': 1, 'dark': 2, 'blank': 0}
    
    ERROR01 = 'error: light/blank/dark/size non-integer'
    ERROR02 = 'error: light/blank/dark/size out of bounds'
    ERROR03 = 'error: light/blank/dark not unique'
    ERROR04 = 'error: odd size'
    
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
        result['tokens']['light'] = light
        
    if 'dark' in parms:
        try:
            dark = int(parms['dark'])
        except:
        #If value of 'dark' is not integer, return corresponding error message
            return {'status': ERROR01}
    
    return result
