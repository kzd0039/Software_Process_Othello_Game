'''
    Created on Mar 11, 2020
    @author: Kun Ding
    
    Modified on Mar 12, 2020
    @author: Kun Ding
'''
import hashlib


def _create(parms):
    #New an empty result dictionary to store the output
    result = {}
    #Set the default value of 'light', 'dark', 'blank' to 1, 2, 0 respectively
    result['tokens'] = { 'light': 1, 'dark': 2, 'blank': 0}
    
    
    #Define error messages
    ERROR01 = 'error: value of light/blank/dark should be integers only'
    ERROR02 = 'error: value of light/blank/dark out of bounds'
    ERROR03 = 'error: value of light/blank/dark should be distinct'
    ERROR04 = 'error: value of size should be even'
    
    
    #Validate input
    if 'light' in parms:
        light = parms['light']
        #If value of 'light' is not integer, return corresponding error message
        if not(isinstance(light, int)):
            return {'status': ERROR01}
        #If value of 'light' is not in range [0,9], return corresponding error message
        if light > 9 or light < 0:
            return {'status': ERROR02}
        #Overwrite the value of 'light'
        result['tokens']['light'] = light
        
        
    if 'dark' in parms:
        dark = parms['dark']
        #If value of 'dark' is not integer, return corresponding error message
        if not(isinstance(dark, int)):
            return {'status': ERROR01}
        #If value of 'dark' is not in range [0,9], return corresponding error message 
        if dark > 9 or dark < 0:
            return {'status': ERROR02}
        #If value of 'dark' equals to the value of 'light', return corresponding error message
        if dark == result['tokens']['light']:
            return {'status': ERROR03}
        #overwrite the value of dark
        result['tokens']['dark'] = dark
        
        
    if 'blank' in parms:
        blank = parms['blank']
        #If value of 'blank' is not integer, return corresponding error message
        if not(isinstance(blank, int)):
            return {'status': ERROR01}
        #If value of 'blank' is not in range [0,9], return corresponding error message 
        if blank > 9 or blank < 0:
            return {'status': ERROR02}
        #If value of 'dark' equals to the value of 'light' or 'dark', return corresponding error message
        if blank == result['tokens']['dark'] or blank == result['tokens']['light']:
            return {'status': ERROR03}
        #overwrite the value of blank
        result['tokens']['blank'] = blank
        
        
    if 'size' in parms:
        size = parms['size']
        #If value of 'size' is not integer, return corresponding error message
        if not(isinstance(size, int)):
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
        
        
    light = result['tokens']['light']
    dark = result['tokens']['dark']
    blank = result['tokens']['blank']
    
    
    #Construct 'board' with all 'blank' tokens
    result['board'] = [blank]* (size ** 2)
    #Calculate the index of the four tokens in the center of the board
    left_top = (size ** 2)//2 - 1
    right_top = left_top + 1
    left_bottom = left_top + size
    right_bottom = left_bottom + 1
    #Place 'light' at left_top and right_bottom, place 'dark oat right_top and left_bottom
    result['board'][left_top] = light
    result['board'][right_top] = dark
    result['board'][left_bottom] = dark
    result['board'][right_bottom] = light

    
    #Construct the string for calculation of 'integrity'
    string = ''.join(str(x) for x in result['board']) 
    string = string + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
    #Calculate the 'integrity' 
    result['integrity'] = hashlib.sha256(string.encode()).hexdigest()
    
    
    #Add 'status' to result dictionary
    result['status'] = 'ok'    
    
    
    #return result to universe
    return result

