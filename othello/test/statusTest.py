"""
    Created for integration test of status
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    Modified: Mar 29, 2020
    Modified: Mar 30, 2020
    @Author: Kun Ding
"""

import unittest
import othello.status as status

class statusTest(unittest.TestCase):
    def setUp(self):
        self.inputDictionary = {}
        self.error1 = 'error: light/blank/dark non-integer'
        self.error2 = 'error: light/blank/dark out of bounds'
        self.error3 = 'error: light/blank/dark not unique'
        self.error4 = 'error: missing board'
        self.error5 = 'error: non-square board'
        self.error6 = 'error: odd board'
        self.error7 = 'error: board with non-light/dark/blank tokens'
        self.error8 = 'error: missing integrity'
        self.error9 = 'error: invalid integrity'
        self.error10 = 'error: board size out of bounds'
        self.error11 = 'error: short integrity'
        self.error12 = 'error: long integrity'
        
    def tearDown(self):
        self.inputDictionary = {}
        
    def setOperation(self, op):
        self.inputDictionary['op'] = op
        
    def setLight(self, light):
        self.inputDictionary['light'] = light
        
    def setDark(self, dark):
        self.inputDictionary['dark'] = dark
        
    def setBlank(self, blank):
        self.inputDictionary['blank'] = blank
    
    def setBoard(self, board):
        self.inputDictionary['board'] = board
        
    def setIntegrity(self, integrity):
        self.inputDictionary['integrity'] = integrity
        
    def setExtra(self, extra):
        self.inputDictionary['extra'] = extra
    
    
    
    def test200_010(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,1,2,0,0,
                 0,0,2,1,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)
     
    def test200_020(self):
        self.setOperation('status')
        self.setLight('9')
        self.setDark('2')
        self.setBlank('0')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,9,2,0,0,
                 0,0,2,9,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)

    def test200_021(self):
        self.setOperation('status')
        self.setLight('0')
        self.setDark('2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,0,2,1,1,
                 1,1,2,0,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = '1b7e612b959852acbaf6b55d3f6b8dab2cdc32248a58a89dcf022ae80e5b36de'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
        
    def test200_022(self):
        self.setOperation('status')
        self.setDark('2')
        self.setBlank('3')
        board = [3,3,3,3,3,3,
                 3,3,3,3,3,3,
                 3,3,1,2,3,3,
                 3,3,2,1,3,3,
                 3,3,3,3,3,3,
                 3,3,3,3,3,3]
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
                
                
    def test200_030(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('0')
        self.setBlank('9')
        board = [9,9,9,9,9,9,
                 9,9,9,9,9,9,
                 9,9,5,0,9,9,
                 9,9,0,5,9,9,
                 9,9,9,9,9,9,
                 9,9,9,9,9,9]
        integrity = '85c972c79b667135f99ad9380f4af4a7495c5b5de3768c9cb36c4bc73f0da08a'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
    
    def test200_031(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('9')
        self.setBlank('3')
        board = [3,3,3,3,3,3,
                 3,3,3,3,3,3,
                 3,3,5,9,3,3,
                 3,3,9,5,3,3,
                 3,3,3,3,3,3,
                 3,3,3,3,3,3]
        integrity = '34932b7f4bbafed18cf99e367e29407e6aae8b49b2ced711f31e429e7efc2a12'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
    def test200_032(self):
        self.setOperation('status')
        self.setLight('5')
        self.setBlank('3')
        board = [3,3,3,3,3,3,
                 3,3,3,3,3,3,
                 3,3,5,2,3,3,
                 3,3,2,5,3,3,
                 3,3,3,3,3,3,
                 3,3,3,3,3,3]
        integrity = 'a348c2dae89e65378fc64d889b1d394819c021b2e4cccb37310bbef9335bb900'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)
        
        
    def test200_040(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('6')
        self.setBlank('0')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,5,6,0,0,
                 0,0,6,5,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)      

    def test200_041(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('6')
        self.setBlank('9')
        board = [9,9,9,9,9,9,
                 9,9,9,9,9,9,
                 9,9,5,6,9,9,
                 9,9,6,5,9,9,
                 9,9,9,9,9,9,
                 9,9,9,9,9,9]
        integrity = '5b698f38d9d1c1754df196ee688f3900ceba9d074cb74b5e17c19a197b69bf02'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
        
          
    def test200_042(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('6')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,5,6,0,0,
                 0,0,6,5,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
    def test200_050(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,1,2,0,0,
                 0,0,2,1,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)  
    
    def test200_051(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        integrity = '5df1fd1ccbd0dc74d65ab00d4d62f2e21c2def95dc47e7c73751986cdb5e8710'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
        
    def test200_060(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board = [3,3,3,3,3,3,
                 3,3,3,3,3,3,
                 3,3,1,2,3,3,
                 3,3,2,1,3,3,
                 3,3,3,3,3,3,
                 3,3,3,3,3,3]
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)  
        
#     def test200_061(self):
#         self.setOperation('status')
#         self.setLight('1')
#         self.setDark('2')
#         self.setBlank('3')
#         board = [3,3,3,3,3,3,
#                  3,3,3,3,3,3,
#                  3,3,1,2,3,3,
#                  3,3,2,1,3,3,
#                  3,3,3,3,3,3,
#                  3,3,3,3,3,3]
#         integrity = '66271cbb9037c515e73be3a74a37259a179f2d2861cf4e82130cd579a2141093'
#         self.setBoard(board)
#         self.setIntegrity(integrity)
#      
#         correct = {'status': 'ok'}
#         result = status._status(self.inputDictionary)
#         self.assertEqual(correct, result)   

   
    def test200_070(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,1,2,0,0,
                 0,0,2,1,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result) 
        

    def test200_071(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        board =  [0,1,1,1,1,0,
                  1,1,1,1,1,1,
                  1,1,1,1,1,1,
                  1,1,1,2,1,1,
                  1,1,1,1,1,1,
                  0,1,1,1,1,0]
        integrity = 'e2f7b8593ebadc126833074a7d8653d3c12c36ab3b7622a9cc6ac5dc1a0d9698'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': 'dark'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)         
      
      
    def test200_072(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board = [2,2,2,2,2,2,
                 2,2,2,2,2,2,
                 2,2,1,2,2,2,
                 2,2,2,2,2,2,
                 2,2,2,2,2,2,
                 2,2,2,2,2,3]
        integrity = '7c53df9ff782bbbff544d876f4d69a1d87d5864295c0e4a6bf29e6a7ee5a96fc'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': 'light'}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
        
#     def test200_073(self):
#         self.setOperation('status')
#         self.setLight('1')
#         self.setDark('2')
#         self.setBlank('0')
#         board = [1,1,1,1,1,1,1,1, 
#                  1,1,1,1,1,1,1,1,
#                  1,1,1,1,1,1,1,1,
#                  1,1,1,1,1,1,1,0, 
#                  1,1,1,1,1,1,0,0,
#                  1,1,1,1,1,1,0,2,
#                  1,1,1,1,1,1,1,0,
#                  1,1,1,1,1,1,1,1]
#         integrity = '8a1c0659575e8cdd01b2e4ff3f431c845e7e7960279bb7abfaa5465e4a755354'
#         self.setBoard(board)
#         self.setIntegrity(integrity)
#      
#         correct = {'status': 'end'}
#         result = status._status(self.inputDictionary)
#         self.assertEqual(correct, result)    
    
    
        
    #Sad path
    def test200_900(self):
        self.setOperation('status')
        self.setLight('10')
        self.setDark('2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,10,2,1,1,
                 1,1,2,10,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = 'b71bf3bee30fb8c3caa49752bcf9656870cfbd3bec4e4353e1e491054bf11c2f'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result) 
        
    def test200_901(self):
        self.setOperation('status')
        self.setLight('-1')
        self.setDark('2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,-1,2,1,1,
                 1,1,2,-1,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = 'f31631fdc7ba5ecd3096a306dbc7e43a9bc13fa781b91d83c36057f5050a51da'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result) 
        
     
    def test200_902(self):
        self.setOperation('status')
        self.setLight('X')
        self.setDark('2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,'X',2,1,1,
                 1,1,2,'X',1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = '8959fc376b23af1520014ef3bef1eb4f924ec692bbbcd9f638245bf85fb0a6da'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
        
    def test200_903(self):
        self.setOperation('status')
        self.setLight(None)
        self.setDark('2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,3,2,1,1,
                 1,1,2,3,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = '1cc0050055aa122edbb536cc63dfe515e6a55132a42a6c8fa41349ab6e572c6a'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
        
        
    def test200_910(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('10')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,5,10,1,1,
                 1,1,10,5,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = 'e8a244c301df58429d82070942fe05dff389162c0aeec8383e3c82863ae09c62'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
    def test200_911(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('-1')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,5,-1,1,1,
                 1,1,-1,5,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = '301e0f00c1b83b65adc1d4fd5e87aaf7f594aa20842ab1df86a6be2e144367db'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
    
    def test200_912(self):
        self.setOperation('status')
        self.setLight('5')
        self.setDark('1.2')
        self.setBlank('1')
        board = [1,1,1,1,1,1,
                 1,1,1,1,1,1,
                 1,1,5,1.2,1,1,
                 1,1,1.2,5,1,1,
                 1,1,1,1,1,1,
                 1,1,1,1,1,1]
        integrity = 'e62a2ec6eb082391a6a5664b4f4dbd8130e43d6589267b19b831423bfcde4a9d'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)      
        
    def test200_913(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark(None)
        self.setBlank('3')
        board = [3,3,3,3,3,3,
                 3,3,3,3,3,3,
                 3,3,1,2,3,3,
                 3,3,2,1,3,3,
                 3,3,3,3,3,3,
                 3,3,3,3,3,3]
        integrity = '5d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)         
        
    def test200_920(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('10')
        board = [10,10,10,10,10,10,10,10,10,10,
                 10,10,10,10,1,2,10,10,10,10,2,1,
                 10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        integrity = '530242aec98aa07d3c025b9101bd5b840527cd9b03302641da18c801d70c37e8'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)      
        
      
    def test200_921(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('-1')
        board = [-1,-1,-1,-1,-1,-1, -1,-1,-1,-1,-1,-1,
                 -1,-1,1,2,-1,-1,-1,-1,2,1,-1,-1,-1,-1,
                 -1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        integrity = '2e226315d3fc18cf5771b45ae78bfe7be9510ee98b6e566e382f8a70861c8e7d'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error2}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
    def test200_922(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('1E5')
        board = ['1E5','1E5','1E5','1E5','1E5','1E5','1E5','1E5','1E5','1E5',
                 '1E5','1E5','1E5','1E5',1,2,'1E5','1E5','1E5','1E5',2,1,
                 '1E5','1E5','1E5','1E5','1E5','1E5','1E5','1E5','1E5',
                 '1E5','1E5','1E5','1E5','1E5']
        integrity = 'fe62b7f99befb02e21c50cc755a68ef80fb59d56224b02a1f2888e0830454773'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
              
      
    def test200_923(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank(None)
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,1,2,0,0,
                 0,0,2,1,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0]
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error1}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)       
       
    def test200_930(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3]
        integrity = '9d43a04297202bccc81a13b6857179269c0fe33e5227c6569286d54d82493ba6'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error5}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)    
    
        
    def test200_933(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        integrity = '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'
        self.setBoard(board)
        self.setIntegrity(integrity)
     
        correct = {'status': self.error6}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)       
        
    def test200_934(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        integrity = '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'
        self.setIntegrity(integrity)
     
        correct = {'status': self.error4}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)   
        
    def test200_935(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        integrity = '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'
        self.setIntegrity(integrity)
        self.setBoard(None)
        correct = {'status': self.error4}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)      
        
    def test200_940(self):
        self.setOperation('status')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board=[3,3,3,3,3,3,
               3,3,3,3,3,3,
               3,3,1,2,3,3,
               3,3,2,1,3,3,
               3,3,3,3,3,3,
               3,3,3,3,3,3]
        self.setBoard(board)
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'
        self.setIntegrity(integrity)
        self.setBoard(None)
        correct = {'status': self.error11}
        result = status._status(self.inputDictionary)
        self.assertEqual(correct, result)         
        
        
        
        
        