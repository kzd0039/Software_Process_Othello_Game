'''
    Created to test place
    Baselined: April 25, 2020
'''

import unittest
import othello.place as place

class statusTest(unittest.TestCase):
    def setUp(self):
        self.inputDictionary = {}
        self.error1 = 'error: light/blank/dark out of bounds'
        self.error2 = 'error: light/blank/dark non-integer'
#         self.error3 = 'error: light/blank/dark not unique'
#         self.error4 = 'error: missing board'
#         self.error5 = 'error: non-square board'
#         self.error6 = 'error: odd board'
#         self.error7 = 'error: board with non-light/dark/blank tokens'
#         self.error8 = 'error: missing integrity'
#         self.error9 = 'error: invalid integrity'
#         self.error10 = 'error: board size out of bounds'
#         self.error11 = 'error: short integrity'
#         self.error12 = 'error: long integrity'
#         
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
        
    def setLocation(self, location):
        self.inputDictionary['location'] = location
        
        
    def setExtra(self, extra):
        self.inputDictionary['extra'] = extra
        
        
        
        
        
    def test300_900LightNonInteger(self):
        self.setLight('X')
        
        correct = {'error': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
        
        
        