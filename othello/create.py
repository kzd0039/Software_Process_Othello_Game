'''
    Created on Mar 11, 2020
    @author: Kun Ding
    
    Modified on Mar 12, 2020
    @author: Kun Ding
'''

def _create(parms):
    #new a result dictionary to store the output and set all the default value
    result = {'board':[],
              'tokens':{'light': 1, 'dark': 2, 'blank': 0},
              'status': 'ok',
              'integrity': ''}
    
    #define error messages
    error1 = 'error: value of light/blank/dark should be integers only'
    error2 = 'error: value of light/blank/dark out of bounds'
    error3 = 'error: value of light/blank/dark should be distinct'
    error4 = 'error: value of size should be even'
    
    #validate input
    if 'light' in parms:
        light = parms['light']
        if not(isinstance(light, int)):
            return {'status': error1}
        if light > 9 or light < 0:
            return {'status': error2}
        #overwrite the value of light
        result['tokens']['light'] = light
        
        
    if 'dark' in parms:
        dark = parms['dark']
        if not(isinstance(dark, int)):
            return {'status': error1}
        if dark > 9 or dark < 0:
            return {'status': error2}
        if dark == result['tokens']['light']:
            return {'status': error3}
        #overwrite the value of dark
        result['tokens']['dark'] = dark
        
        
    if 'blank' in parms:
        blank = parms['blank']
        if not(isinstance(blank, int)):
            return {'status': error1}
        if blank > 9 or blank < 0:
            return {'status': error2}
        if blank == result['tokens']['dark'] or blank == result['tokens']['light']:
            return {'status': error3}
        #overwrite the value of blank
        result['tokens']['blank'] = blank
        
    if 'size' in parms:
        size = parms['size']
        if not(isinstance(size, int)):
            return {'status': error1}
        if size > 16 or size < 6:
            return {'status': error2}
        if size % 2 != 0:
            return {'status': error4}
        #overwrite the value of board
        light = result['tokens']['light']
        dark = result['tokens']['dark']
        blank = result['tokens']['blank']
        
        result['board'] = [blank]* (size ** 2)
        index_light= ((size // 2) - 1) * size + size // 2 - 1
        result['board'][index_light] = light
        result['board'][index_light + 1] = dark
        result['board'][index_light + size] = dark
        result['board'][index_light + size + 1] = light
        
        
        
    #return result to universe
    return result