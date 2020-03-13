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
    
    #100 create
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #        inputs:        
    #                    parms['light'] -> integer .GE.0 .LE.9 
    #        outputs:    float .GT. 0 .LE. 1.0
    #    Happy path analysis:
    #       n:       nominal value    n=6
    #                low bound        n=3
    #        t:      nominal value    t=1.4398
    #                low bound        t>0.0
    #        tails:  value 1          tails = 1
    #                value 2          tails = 2
    #                missing tails
    #        output:
    #                The output is an interaction of t x tails x n:
    #                    nominal t, 1 tail
    #                    nominal t, 2 tails
    #                    low n, low t, 1 tail
    #                    low n, low t, 2 tails
    #                    high n, low t, 1 tail
    #                    high n, low t, 2 tails
    #                    low n, high t, 1 tail
    #                    low n, high t, 2 tails
    #                    high n, high t, 1 tail
    #                    high n, high t, 2 tails
    #                    nominal t, default tails
    #    Sad path analysis:
    #        n:      missing n
    #                out-of-bound n   n<3
    #                non-integer n    n = 2.5
    #        t:      missing t
    #                out-of-bounds n  t<0.0
    #                non-numeric t    t="abc"
    #        tails:  invalid tails    tails = 3
    #
    # Happy path
        
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
        
        
        
        
        
        
        
    