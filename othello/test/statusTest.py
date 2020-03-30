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

#     def test_tdd_02(self):
#         board = [0,1,1,1,1,0,
#                  1,1,1,1,1,1,
#                  1,1,1,1,1,1,
#                  1,1,1,2,1,1,
#                  1,1,1,1,1,1,
#                  0,1,1,1,1,0]
#        
#         integrity='e2f7b8593ebadc126833074a7d8653d3c12c36ab3b7622a9cc6ac5dc1a0d9698'
#         self.setBoard(board)
#         self.setIntegrity(integrity)
#     
#         correct = {'status': 'dark'}
#         result = status._status(self.inputDictionary)
#     
#         self.assertEqual(correct, result)
#         
#         
#     def test_tdd_03(self):
#         board = [2,2,2,2,2,2,
#                  2,2,2,2,2,2,
#                  2,2,1,2,2,2,
#                  2,2,2,2,2,2,
#                  2,2,2,2,2,2,
#                  2,2,2,2,2,3]
#         self.setLight('1')
#         self.setDark('2')
#         self.setBlank('3')
#         integrity='7c53df9ff782bbbff544d876f4d69a1d87d5864295c0e4a6bf29e6a7ee5a96fc'
#         self.setBoard(board)
#         self.setIntegrity(integrity)
#     
#         correct = {'status': 'light'}
#         result = status._status(self.inputDictionary)
#     
#         self.assertEqual(correct, result)
#             
#     def test_tdd_04(self):
#         board = [1,1,1,1,1,1,1,1, 
#                  1,1,1,1,1,1,1,1,
#                  1,1,1,1,1,1,1,1,
#                  1,1,1,1,1,1,1,0, 
#                  1,1,1,1,1,1,0,0,
#                  1,1,1,1,1,1,0,2,
#                  1,1,1,1,1,1,1,0,
#                  1,1,1,1,1,1,1,1]  
#         
#         self.setLight('1')
#         self.setDark('2')
#         self.setBlank('0')
#         integrity='8a1c0659575e8cdd01b2e4ff3f431c845e7e7960279bb7abfaa5465e4a755354'
#         self.setBoard(board)
#         self.setIntegrity(integrity)
#     
#         correct = {'status': 'end'}
#         result = status._status(self.inputDictionary)
#     
#         self.assertEqual(correct, result)
               

        
        
        
        
    