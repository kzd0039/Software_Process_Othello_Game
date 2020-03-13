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
        self.error1 = 'error: value of light/blank/dark should be integers only'
        self.error2 = 'error: value of light/blank/dark out of bounds'
        self.error3 = 'error: value of light/blank/dark should be distinct'
        self.error4 = 'error: value of size should be even'
        self.inputDictionary = {}
        
    def tearDown(self):
        self.inputDictionary = {}
    
    def setLight(self, light):
        self.inputDictionary['light'] = light
        
    def setDark(self, dark):
        self.inputDictionary['dark'] = dark
        
    def setBlank(self, blank):
        self.inputDictionary['blank'] = blank
    
    def setSize(self, size):
        self.inputDictionary['size'] = size
    
    
        
    def test100_010(self):
        correct = { 'board':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 6, 5, 1, 1, 1, 1, 
                             1, 1, 1, 1, 5, 6, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 6, 'dark': 5, 'blank': 1}, 
                    'status': 'ok', 
                    'integrity': 'd0f18c5b412ab1dbf89da19baa33cc35f4a7dd0619ce7b7dcb2381d2cb14a412'}
        self.setLight(6)
        self.setDark(5)
        self.setBlank(1)
        self.setSize(10)
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
        
        
        
        
        
        
    