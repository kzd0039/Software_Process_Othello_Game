'''
    Created to place token on board
    Baselined: April 25, 2020
    Modified: April 26, 2020
    Modified: April 27, 2020
    @Author: Kun Ding
'''


import math
import collections
import hashlib

def _place(parms):
    ERROR01 = 'error: light/blank/dark not unique'
    ERROR02 = 'error: missing board'
    ERROR03 = 'error: missing location'
    ERROR04 = 'error: missing integrity'
    ERROR05 = 'error: location out-of-bound'
    ERROR06 = 'error: location occupied'
    ERROR07 = 'error: incorrect location'
    
    
    #set default value of light, dark and blank
    tokens = {'light':1, 'dark':2, 'blank':0}
    #if light in parms, check if value of light if valid
    if 'light' in parms:
        r = isValidTokens(parms['light'])
        if not isinstance(r, int):
            return r
        tokens['light'] = r
    #if dark in parms, check if value of dark is valid   
    if 'dark' in parms:
        r = isValidTokens(parms['dark'])
        if not isinstance(r, int):
            return r
        tokens['dark'] = r
    #if blank in parms, check if value of blank is valid
    if 'blank' in parms:
        r = isValidTokens(parms['blank'])
        if not isinstance(r, int):
            return r
        tokens['blank'] = r
    
    
    
    light = str(tokens['light'])
    dark = str(tokens['dark'])
    blank = str(tokens['blank'])
  
    
    
    #if board is not in parms or its value is null, return error message
    if 'board' not in parms or parms['board'] == None:
        return {'status': ERROR02}
    #if board is in parms, check if its value is valid
    board = isValidBoard(tokens, parms['board'])
    if not isinstance(board, list):
        return board
    
    
    size = int(math.sqrt(len(board)))
    
    #if location is not in parms or its value is null, return error message
    if 'location' not in parms or parms['location'] == None:
        return {'status': ERROR03}
    #if location is in parms, check if its value is valid
    location = isValidLocation(parms['location'])
    if not isinstance(location, list):
        return location
    
    #check if value of light, dark and blank is unique
    if light == dark or dark == blank or light == blank:
        return {'status': ERROR01}
    
    #if integrity is not in parms or its value is null, return error message
    if 'integrity' not in parms or parms['integrity'] == None:
        return {'status': ERROR04}
    #check if value of integrity is correct, return error if not.
    #If correct, store the current token to place and also the next token to place
    result = isValidIntegrity(parms['integrity'], board, light, dark, blank, size)
    if not isinstance(result, list):
        return result
    token_to_place = result[0]
    opposite = result[1]
    
    #convert the row and column of the token position to 0 based. 
    current_row = location[0] - 1
    current_column = location[1] - 1
    #If the token position is out of range or is nor correct format, return error message
    next_token_position = get_index(current_row, current_column, size)
    if next_token_position == -1:
        return {'status': ERROR05}
    #if the token is already occupied by light or dark, return error message
    if board[next_token_position] != blank:
        return {'status': ERROR06}
    
    #Create a list to store eight directions, down, up, right, left, down-left, down-right, up-left, up-right 
    Directions = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1]]
    #new the list to store end positions, between which and the position identified by location, the tokens should reverse.
    pair_position = [ ]
    
    #iterate the 8 directions and store the end position if this position is valid
    for direction in Directions:
        row = current_row + direction[0]
        column = current_column + direction[1]
        current_index = get_index(row, column, size)
        current_token = board[current_index]
        while current_index != -1 and current_token == opposite:
            row += direction[0]
            column += direction[1]
            current_index = get_index(row, column, size)
            current_token = board[current_index]
            
        if current_index != -1 and current_token == token_to_place:
            pair_position.append([row, column, direction])
    
    #If no valid directions, which means after the token is placed, no other tokens should flip, return error
    if not pair_position:
        return {'status': ERROR07} 
    
    
    #new the dictionary to store output
    result = { }
    
    #flip the tokens between the token to place and the valid end positions
    for x in pair_position:
        destination_row = x[0]
        destination_column = x[1]
        direction = x[2]
        c_row = current_row
        c_column = current_column
        while not(c_row == destination_row and c_column == destination_column):
            board[get_index(c_row, c_column, size)] = token_to_place
            c_row += direction[0]
            c_column += direction[1]
    #store the value of board in output dictionary    
    result['board'] = '[' + ','.join(board) +']'
    
    #Create dictionary to store the number of light and dark that could be placed on current board
    next_tokens = {light:0,dark:0}
    
    #iterate all the positions and 8 directions for each, store the number of light and dark tokens could be placed next
    for i in range(size):
        for j in range(size):
            #Get the current index based on the row, column and size of the board.
            index = get_index(i,j,size)
            #If the token is blank, means it is possible to place a light or dark.
            if board[index] == blank:
                #From this token, check eight directions one by one.
                for direction in Directions:
                    #Create list to keep track of tokens as it moves.
                    stack = [ ]
                    #If is_valid() return the token that is dark or light, update the total number
                    key = is_valid(i,j,size,board,tokens,stack,direction)
                    if key in next_tokens:
                        next_tokens[key] += 1
    
    #if both value are greater than 0, next_token can be light or dark, reverse the next player
    if next_tokens[light] > 0 and next_tokens[dark] > 0:
        result['status'] = 'ok'
        next_token = opposite
    #if only light can be placed on board, light must be the next player   
    elif next_tokens[light] > 0 and next_tokens[dark]==0:
        result['status'] = 'ok'
        next_token = light
    #if only dark can be placed on board, dark must be the next player   
    elif next_tokens[dark] > 0 and next_tokens[light]==0:
        result['status'] = 'ok'
        next_token = dark
    #if the game is end, set next player to dark and count the board 
    else:
        next_token = dark
        count_board = collections.Counter(board)
        result['status'] = 'end:' + str(count_board[light]) + '/' + str(count_board[dark])
        
    #calculate integrity and return result
    output_integrity = integrityCalculation(board, light, dark, blank, next_token, size)
    result['integrity'] = output_integrity
    return result 
        
    
    
def isValidTokens(token):
    #validate tokens, the must of token must be integer and in the range[0,9]
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


def isValidBoard(tokens, input_board):
    #validate board. board length must be squared value of a even integer between [6,16] and only contains light, dark and blank tokens 
    ERROR01 = 'error: invalid board'
    ERROR02 = 'error: non-square board'
    ERROR03 = 'error: board size out of bounds'
    ERROR04 = 'error: odd board'
    ERROR05 = 'error: board with non-light/dark/blank tokens'
    
    try:
        board = input_board[1:-1].split(',')
    except:
        return {'status': ERROR01}
    
    len_board = len(board)
   
    size = int(math.sqrt(len_board))
   
    if size**2 != len_board:   
        return {'status': ERROR02}
    
    if size < 6 or size > 16:
        return {'status': ERROR03}

    if size%2 != 0:
        return {'status': ERROR04}
    
    light = str(tokens['light'])
    dark = str(tokens['dark'])
    blank = str(tokens['blank'])
    
    count = collections.Counter(board)
    if set(count.keys()) != set([light, dark, blank]):
        return {'status': ERROR05}
    
    return board
  

def isValidLocation(input_location):
    #validate location. location must be string in 'x:y' format, where x and y are integers
    ERROR01 = 'error: invalid location'
    try:
        location =[int(x) for x in input_location.split(':')]
    except:
        return {'status': ERROR01}
    return location
    

def integrityCalculation(board, light, dark, blank, next_token, size):
    #calculate integrity. 
    string = ''.join(board[i+j*size] for i in range(size) for j in range(size)) \
            + '/' + light +'/' +  dark +'/' +  blank + '/' +  next_token
    return hashlib.sha256(string.encode()).hexdigest()


def isValidIntegrity(input_integrity, board, light, dark, blank,size):
    #validate integrity. It must match either the one who's next_token is light or the one who's next_token is dark.
    ERROR01 = 'error: invalid integrity'
    ERROR02 = 'error: incorrect integrity'
    
    if len(input_integrity) != 64:
        return{'status': ERROR01}
        
    integrity1 = integrityCalculation(board, light, dark, blank, light, size)
    integrity2 = integrityCalculation(board, light, dark, blank, dark, size)
    
    if input_integrity == integrity1:
        return [light,dark]
    if input_integrity == integrity2:
        return [dark,light]
    return {'status': ERROR02}


def get_index(row, column, size):
    #check if the row is column is valid, return -1 if out of bounds, return index in the board if valid.
    if row >= 0 and row <size and column >= 0 and column < size:
        return row*size + column
    else:
        return -1


def is_valid(row, column, size, board, tokens, stack, direction):
    #Move forward according to the direction
    row += direction[0]
    column += direction[1]
    #if index is out of bounds, return -1 to show current path is invalid
    i = get_index(row, column, size)
    if i == -1:
        return -1
    
    current = board[i]
    #If current token is blank, return -1 to show current path is invalid
    if current == str(tokens['blank']):
        return -1
    #If the current token is not the same with previous, return current token to show that this token can place on the original blank token
    if stack and current != stack[-1]:
        return current
    else:
        #If the current is the same with previous, store the current token and keep moving
        stack.append(current)
        return is_valid(row, column, size, board, tokens, stack, direction)
   













