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
    error1 = 'error: light/blank/dark should be integers only'
    error2 = 'error: number out of bounds'
    error3 = 'error: light/blank/dark should be distinct'
    
    #validate input
    if 'light' in parms:
        if not(isinstance(parms['light'], int)):
            return {'status': error1}
    
    #return result to universe
    return result
