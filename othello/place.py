'''
    Created to place token on board
    Baselined: April 25, 2020
'''




def _place(parms):
    token = {'light':1, 'dark':2, 'blank':0}
    if 'light' in parms:
        r = isValidTokens(parms['light'])
        if  r != True:
            return r


def isValidTokens(token):
    ERROR01 = 'error: light/blank/dark non-integer'
    ERROR02 = 'error: light/blank/dark out of bounds'
    try:
        int_token = int(token)
    except:
    #If value of 'light' is not integer, return corresponding error message
        return {'error': ERROR01}
    #If value of 'light' is not in range [0,9], return corresponding error message
    if int_token > 9 or int_token < 0:
        return {'status': ERROR02}
#     #Overwrite the value of 'light'
#     tokens['light'] = light