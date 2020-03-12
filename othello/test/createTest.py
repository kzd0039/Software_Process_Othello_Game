'''
    Created on Mar 11, 2020
    @author: Kun Ding
    
    Modified on Mar 12, 2020
    @author: Kun Ding
'''

import unittest
import othello.create as create

class createTest(unittest.TestCase):
    def setUp(self):
        self.nominalLight = 1
        self.nominalDark = 2
        self.nominalBlank = 0
        self.nominalSize = 8
        self.nominalOperation = 'create'
        self.error1 = 'error: value of light/blank/dark should be integers only'
        self.error2 = 'error: value of light/blank/dark out of bounds'
        self.error3 = 'error: value of light/blank/dark should be distinct'
        self.inputDictionary = {}
        
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
    
    def setSize(self, size):
        self.inputDictionary['size'] = size
    
    
    def test100_010(self):
#         correct = {}
#         correct['board'] = []
#         correct['tokens'] = {'light': 1, 'dark': 2, 'blank': 0}
#         correct['status'] = 'ok'
#         correct['integrity'] = ''
        correct = {'status': self.error3}
        
        self.setOperation(self.nominalOperation)
        self.setLight(2)
        self.setDark(3)
        self.setBlank(3)
        result = create._create(self.inputDictionary)
        
        self.assertEqual(correct, result)
        
        
        
        
        
        
        
        
    