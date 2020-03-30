"""
    Created for integration test of status
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    Modified: Mar 29, 2020
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
    
    
    
    
    
    
    
    def test_tdd(self):
        board = [0,0,0,0,0,0,
                 0,0,0,0,0,0,
                 0,0,1,2,0,0,
                 0,0,2,1,0,0,
                 0,0,0,0,0,0,
                 0,0,0,0,0,0,]
                 
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': self.error11}
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
               

        
        
        
        
    