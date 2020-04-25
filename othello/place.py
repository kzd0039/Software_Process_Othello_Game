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
    try:
        int_token = int(token)
    except:
    #If value of 'light' is not integer, return corresponding error message
        return {'status': ERROR01}
#     #If value of 'light' is not in range [0,9], return corresponding error message
#     if light > 9 or light < 0:
#         return {'status': ERROR02}
#     #Overwrite the value of 'light'
#     tokens['light'] = light