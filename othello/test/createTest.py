'''
    Created on Mar 11, 2020
    @author: Kun Ding
    
    Modified on Mar 12, 2020
    @author: Kun Ding
    
    Modified on Mar 13, 2020
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
        self.error1 = 'error: value of light/blank/dark must be integers only'
        self.error2 = 'error: value of light/blank/dark out of bounds'
        self.error3 = 'error: value of light/blank/dark must be distinct'
        self.error4 = 'error: value of size must be even'
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
    #        inputs -> dictionary:  
    #                    key        value
    #                    'light' -> integer .GE.0 .LE.9, optional, defaulting to 1, arrives unvalidated 
    #                    'dark'  -> integer .GE.0 .LE.9, optional,  defaulting to 2, arrives unvalidated 
    #                    'blank' -> integer .GE.0 .LE.9, optional,  defaulting to 0, arrives unvalidated 
    #                    'size'  -> even integer .GE.6 .LE.16, optional,  defaulting to 8, arrives unvalidated 
    #        outputs -> dictionary:
    #                    key        value
    #                    'board' -> list of integers,
    #                    'tokens' -> dictionary
    #                                  key       value
    #                                  'light' -> The integer value specified by the light parameter
    #                                  'dark'  -> The integer value specified by the dark parameter
    #                                  'blank' -> The integer value specified by the blank parameter
    #                    'status' -> string, value = 'ok'
    #                    'integrity' -> sha256 hash hexdigest of string formed by 
    #                                   concatenating the string value of each of the playing surface cells in column-major order
    #                                   followed by by the string "/<light>/<dark>/<blank>/<next_player>"
    #                                   <light> is the value specified by the light parameter        
    #                                   <dark> is the value specified by the dark parameter        
    #                                   <blank> is the value specified by the blank parameter        
    #                                   <next_player> At creation, <next_player> is the value associated with the dark parameter.        
    #    Happy path analysis:
    #      
    #    Sad path analysis:
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
        self.setLight('6')
        self.setDark('5')
        self.setBlank('1')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
    
    def test100_020(self):
        correct = { 'board':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 9, 5, 1, 1, 1, 1, 
                             1, 1, 1, 1, 5, 9, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 9, 'dark': 5, 'blank': 1}, 
                    'status': 'ok', 
                    'integrity': '723c769319c6529cf8520336232a9e5d281be77df1455c6ceb10a5d1d4733236'}
        self.setLight('9')
        self.setDark('5')
        self.setBlank('1')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)    
        
    def test100_021(self):
        correct = { 'board':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 0, 5, 1, 1, 1, 1, 
                             1, 1, 1, 1, 5, 0, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                    'tokens': {'light': 0, 'dark': 5, 'blank': 1}, 
                    'status': 'ok', 
                    'integrity': '4bd2efa7e0d5f13551f7277950e45b6fcfe7d5159b80823a5dcbdf57abb4d83a'}
        self.setLight('0')
        self.setDark('5')
        self.setBlank('1')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)  
              
    #Sad path
    def test100_900(self):
        correct = {'status': self.error2}
        self.setLight('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_901(self):
        correct = {'status': self.error2}
        self.setLight('-1')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_902(self):
        correct = {'status': self.error1}
        self.setLight('w')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
        
        
    