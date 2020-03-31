'''
    Created to implement operation create
    Baselined: 11 Mar, 2020 
    Modified: 12 Mar, 2020
    Modified: 13 Mar, 2020
    Modified: 28 Mar, 2020
    Modified: 30 Mar, 2020
    @author: Kun Ding
'''

import hashlib

def _create(parms):
    #New an empty result dictionary to store the output
    result = {}
    #Set the default value of 'light', 'dark', 'blank' to 1, 2, 0 respectively
    result['tokens'] = {'light': 1, 'dark': 2, 'blank': 0}
    
    
    #Define error messages
    ERROR01 = 'error: light/blank/dark/size non-integer'
    ERROR02 = 'error: light/blank/dark/size out of bounds'
    ERROR03 = 'error: light/blank/dark not unique'
    ERROR04 = 'error: odd size'
    
    
    #Validate input
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
        #If value of 'dark' is not in range [0,9], return corresponding error message 
        if dark > 9 or dark < 0:
            return {'status': ERROR02}
        #overwrite the value of dark
        result['tokens']['dark'] = dark
        
        
    if 'blank' in parms:
        try:
            blank = int(parms['blank'])
        except:
        #If value of 'blank' is not integer, return corresponding error message
            return {'status': ERROR01}
        #If value of 'blank' is not in range [0,9], return corresponding error message 
        if blank > 9 or blank < 0:
            return {'status': ERROR02}
        #overwrite the value of blank
        result['tokens']['blank'] = blank
    
    light = result['tokens']['light']
    dark = result['tokens']['dark']
    blank = result['tokens']['blank']   
    #If blank, dark or light is not unique, return corresponding error message
    if light == dark or light == blank or dark == blank:
        return {'status': ERROR03}
       
    if 'size' in parms:
        try:  
            size = int(parms['size'])
        except:
        #If value of 'size' is not integer, return corresponding error message
            return {'status': ERROR01}
        #If value of 'size' is not in range [6,16], return corresponding error message
        if size > 16 or size < 6:
            return {'status': ERROR02}
        #If value of 'size' is not even, return corresponding error message
        if size % 2 != 0:
            return {'status': ERROR04}
    #If 'size' is missing, set the size to default value 8
    else:
        size = 8
    
    
    
    #Construct 'board' and set all tokens to blank
    result['board'] = [blank]* (size ** 2)
    #Calculate the index of the four tokens in the center of the board
    left_top = (size ** 2)//2 - size//2 - 1
    right_top = left_top + 1
    left_bottom = left_top + size
    right_bottom = left_bottom + 1
    #Place 'light' at left_top and right_bottom, place 'dark oat right_top and left_bottom
    result['board'][left_top] = light
    result['board'][right_top] = dark
    result['board'][left_bottom] = dark
    result['board'][right_bottom] = light

    
    #Construct the string for calculation of 'integrity'
    string = ''.join(str(result['board'][i+j*size]) for i in range(size) for j in range(size)) 
    string = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
    #Calculate the 'integrity' 
    result['integrity'] = hashlib.sha256(string.encode()).hexdigest()
    
    
    #Add 'status' to result dictionary
    result['status'] = 'ok'    
    
    
    #return result to universe
    return result

