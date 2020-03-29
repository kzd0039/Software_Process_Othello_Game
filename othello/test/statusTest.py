"""
    Created for integration test of status
    Baselined: Mar 25, 2020
    Modified: Mar 28, 2020
    @Author: Kun Ding
"""

import unittest
import othello.status as status

class statusTest(unittest.TestCase):
    def setUp(self):
        self.inputDictionary = {}
        self.error1 = 'error: light/blank/dark/size non-integer'
        self.error2 = 'error: light/blank/dark/size out of bounds'
        self.error3 = 'error: light/blank/dark not unique'
        self.error4 = 'error: missing board'
        self.error5 = 'error: non-square board'
        self.error6 = 'error: odd board'
        self.error7 = 'error: board with non-light/dark/blank tokens'
        self.error8 = 'error: missing integrity'
        self.error9 = 'error: invalid integrity'
        
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
                 0,0,0,0,0,0]
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(board)
        self.setIntegrity(integrity)
    
        correct = {'status': 'ok'}
        result = status._status(self.inputDictionary)
    
        self.assertEqual(correct, result)
       
    
    