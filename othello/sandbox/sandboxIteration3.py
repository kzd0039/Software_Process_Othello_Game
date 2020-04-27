'''
    Created to 
    Baselined: April 25, 2020
'''
import collections
import hashlib
print(isinstance(2, int))

# print(''[1:-1].split(','))
# board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'        
# board = board[1:-1].split(',')
# count = collections.Counter(board)
# print(count)

'''
happy path input-output analysis
'''
def integrityCalculation(board,light,dark,blank,size,next_token):
    string = ''.join(str(board[i+j*size]) for i in range(size) for j in range(size)) + '/' + light + '/' + dark +'/' +  blank + '/' + next_token
    return hashlib.sha256(string.encode()).hexdigest()


#happy path001, input player:dark, output player:light, status:'ok'
board =  [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '2:3'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [0,0,0,0,0,0,
                0,0,2,0,0,0,
                0,0,2,2,0,0,
                0,0,2,1,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy001','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path002, input player:dark, output player:light, status:'ok'
board =  [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '3:2'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,2,2,2,0,0,
                0,0,2,1,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy002','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path003, input player:dark, output player:light, status:'ok'
board =  [0,0,0,0,0,0,
          0,0,2,9,0,0,
          0,0,9,9,0,0,
          0,9,2,9,0,0,
          0,2,0,0,0,0,
          0,0,0,0,0,0]
light = '9'
dark = '2'
blank = '0'
size = 6
location = '4:5'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [0,0,0,0,0,0,
                0,0,2,9,0,0,
                0,0,9,2,0,0,
                0,9,2,2,2,0,
                0,2,0,0,0,0,
                0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy003','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

#happy path004, input player:dark, output player:light, status:'ok'
board =  [1,1,1,1,1,1,1,1,
          1,1,9,3,1,1,1,1,
          1,1,3,3,1,1,1,1,
          1,3,9,3,1,1,1,1,
          1,9,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1]
light = '3'
dark = '9'
blank = '1'
size = 8
location = '4:5'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [1,1,1,1,1,1,1,1,
                1,1,9,3,1,1,1,1,
                1,1,3,9,1,1,1,1,
                1,3,9,9,9,1,1,1,
                1,9,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy004','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path011, input player:light, output player:dark, status:'ok'
board =  [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '3:5'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,1,1,1,0,
                0,0,2,1,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy011','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path012, input player:light, output player:dark, status:'ok'
board =  [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '5:3'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,1,2,0,0,
                0,0,1,1,0,0,
                0,0,1,0,0,0,
                0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy012','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path013, input player:light, output player:dark, status:'ok'
board =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,1,9,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,9,1,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
light = '1'
dark = '9'
blank = '0'
size = 16
location = '8:10'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,
                0,0,0,0,0,0,0,9,1,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy013','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')




#happy path021, input player:light, output player:light, status:'ok'
board =  [0,2,2,2,2,0,
          2,2,2,2,2,2,
          2,2,1,2,2,2,
          2,2,2,2,2,2,
          2,2,2,2,2,2,
          2,2,2,2,2,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '1:1'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [1,2,2,2,2,0,
                2,1,2,2,2,2,
                2,2,1,2,2,2,
                2,2,2,2,2,2,
                2,2,2,2,2,2,
                2,2,2,2,2,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy021','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

#happy path022, input player:light, output player:light, status:'ok'
board =  [9,2,2,2,2,2,2,9,
          2,2,2,2,2,2,2,2,
          2,2,2,2,2,2,2,2,
          2,2,2,2,2,2,2,2,
          2,2,2,1,2,2,2,2,
          2,2,2,2,2,2,2,2,
          2,2,2,2,2,2,2,2,
          2,2,2,2,2,2,2,9]
light = '1'
dark = '2'
blank = '9'
size = 8
location = '1:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [9,2,2,2,2,2,2,1,
                2,2,2,2,2,2,1,2,
                2,2,2,2,2,1,2,2,
                2,2,2,2,1,2,2,2,
                2,2,2,1,2,2,2,2,
                2,2,2,2,2,2,2,2,
                2,2,2,2,2,2,2,2,
                2,2,2,2,2,2,2,9]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, light)
print('happy022','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')




#happy path031, input player:dark, output player:dark, status:'ok'
board =  [0,1,1,1,1,0,
          1,1,1,1,1,1,
          1,1,2,1,1,1,
          1,1,1,1,1,1,
          1,1,1,1,1,1,
          1,1,1,1,1,0]
light = '1'
dark = '2'
blank = '0'
size = 6
location = '1:1'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [2,1,1,1,1,0,
                1,2,1,1,1,1,
                1,1,2,1,1,1,
                1,1,1,1,1,1,
                1,1,1,1,1,1,
                1,1,1,1,1,0]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy031','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')


#happy path032, input player:dark, output player:dark, status:'ok'
board =  [0,1,1,1,1,1,1,0,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,2,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,0]
light = '1'
dark = '2'
blank = '0'
size = 8
location = '8:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [0,1,1,1,1,1,1,0,
                1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,2,1,1,1,1,
                1,1,1,1,2,1,1,1,
                1,1,1,1,1,2,1,1,
                1,1,1,1,1,1,2,1,
                1,1,1,1,1,1,1,2]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy032','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

#happy path041, input player:dark, output player:dark, status:'end'
board =  [1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,2,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,0]
light = '1'
dark = '2'
blank = '0'
size = 8
location = '8:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,2,1,1,1,1,
                1,1,1,1,2,1,1,1,
                1,1,1,1,1,2,1,1,
                1,1,1,1,1,1,2,1,
                1,1,1,1,1,1,1,2]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy041','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

status = 'end:59/5'

#happy path042, input player:dark, output player:dark, status:'end'
board =  [3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,4,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,0]
light = '3'
dark = '4'
blank = '0'
size = 8
location = '8:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,
                3,3,3,4,3,3,3,3,
                3,3,3,3,4,3,3,3,
                3,3,3,3,3,4,3,3,
                3,3,3,3,3,3,4,3,
                3,3,3,3,3,3,3,4]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy042','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

status = 'end:59/5'

#happy path043, input player:dark, output player:dark, status:'end'
board =  [3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,4,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,3,5]
light = '3'
dark = '4'
blank = '5'
size = 10
location = '10:10'
input_integrity = integrityCalculation(board, light, dark, blank, size, dark)
output_board = [3,3,3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,3,3,
                3,3,3,4,3,3,3,3,3,3,
                3,3,3,3,4,3,3,3,3,3,
                3,3,3,3,3,4,3,3,3,3,
                3,3,3,3,3,3,4,3,3,3,
                3,3,3,3,3,3,3,4,3,3,
                3,3,3,3,3,3,3,3,4,3,
                3,3,3,3,3,3,3,3,3,4]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy043','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

status = 'end:93/7'



#happy path051, input player:light, output player:dark, status:'end'
board =  [1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,2,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,0]
light = '2'
dark = '1'
blank = '0'
size = 8
location = '8:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,1,1,1,1,1,
                1,1,1,2,1,1,1,1,
                1,1,1,1,2,1,1,1,
                1,1,1,1,1,2,1,1,
                1,1,1,1,1,1,2,1,
                1,1,1,1,1,1,1,2]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy051','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

status = 'end:5/59'



#happy path052, input player:light, output player:dark, status:'end'
board =  [3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,4,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,3,
          3,3,3,3,3,3,3,0]
light = '4'
dark = '3'
blank = '0'
size = 8
location = '8:8'
input_integrity = integrityCalculation(board, light, dark, blank, size, light)
output_board = [3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,
                3,3,3,3,3,3,3,3,
                3,3,3,4,3,3,3,3,
                3,3,3,3,4,3,3,3,
                3,3,3,3,3,4,3,3,
                3,3,3,3,3,3,4,3,
                3,3,3,3,3,3,3,4]
output_integrity = integrityCalculation(output_board, light, dark, blank, size, dark)
print('happy052','\n',
      'input_integrity:'+input_integrity,'\n',
      'output_integrity:'+output_integrity, '\n')

status = 'end:5/59'

