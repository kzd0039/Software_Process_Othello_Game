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
        
    def setExtra(self, extra):
        self.inputDictionary['extra'] = extra
    
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
        
        
    def test100_022(self):
        correct = { 'board':[3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 1, 5, 3, 3, 3, 3,
                             3, 3, 3, 3, 5, 1, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
                    'tokens': {'light': 1, 'dark': 5, 'blank': 3}, 
                    'status': 'ok', 
                    'integrity': 'f211a92f576794a821bb24f359739b8b42a6a16634005a1e4b32313a6575e2be'}
        self.setDark('5')
        self.setBlank('3')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)    
        
    def test100_030(self):
        correct = { 'board':[4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 3, 9, 4, 4, 4, 4, 
                             4, 4, 4, 4, 9, 3, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                    'tokens': {'light': 3, 'dark': 9, 'blank': 4}, 
                    'status': 'ok', 
                    'integrity': 'a3718ffbc2f822320ee4db10c269a9749859b9952db13ff6b289a6ebd6ce42c6'}
        self.setLight('3')
        self.setDark('9')
        self.setBlank('4')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)     
    
    def test100_031(self):
        correct = { 'board':[4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 3, 0, 4, 4, 4, 4, 
                             4, 4, 4, 4, 0, 3, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                    'tokens': {'light': 3, 'dark': 0, 'blank': 4}, 
                    'status': 'ok', 
                    'integrity': '7bf98e8385a158097f52361dac139bb5882f3eaa48e8146d72d65de5981d2e5e'}
        self.setLight('3')
        self.setDark('0')
        self.setBlank('4')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)  
              
    def test100_032(self):
        correct = { 'board':[4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 3, 2, 4, 4, 4, 4, 
                             4, 4, 4, 4, 2, 3, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                             4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 
                    'tokens': {'light': 3, 'dark': 2, 'blank': 4}, 
                    'status': 'ok', 
                    'integrity': '71f91a7d487c9e9ad69a43269c6a90c449f97fd93848b8493e47a2f6054e7c82'}
        self.setLight('3')
        self.setBlank('4')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)  
              
    def test100_040(self):
        correct = { 'board':[9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 3, 4, 9, 9, 9, 9,
                             9, 9, 9, 9, 4, 3, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                             9, 9, 9, 9, 9, 9, 9, 9, 9, 9,], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 9}, 
                    'status': 'ok', 
                    'integrity': '5b4c82af0cf6a72ab1938b8e5a3c1ce413b9db583d0f974703954427413021d0'}
        self.setLight('3')
        self.setDark('4')
        self.setBlank('9')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)  
        
    def test100_041(self):
        correct = { 'board':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 3, 4, 0, 0, 0, 0,
                             0, 0, 0, 0, 4, 3, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 0}, 
                    'status': 'ok', 
                    'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'}
        self.setLight('3')
        self.setDark('4')
        self.setBlank('0')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result) 
    
    def test100_042(self):
        correct = { 'board':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 3, 4, 0, 0, 0, 0,
                             0, 0, 0, 0, 4, 3, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 0}, 
                    'status': 'ok', 
                    'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'}
        self.setLight('3')
        self.setDark('4')
        self.setSize('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_050(self):
        correct = { 'board':[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                    'status': 'ok', 
                    'integrity': '682b1bac788017f23b846862ce44f2c3efe03a22f49de36085e0e57fc6957416'}
        self.setLight('3')
        self.setDark('4')
        self.setBlank('5')
        self.setSize('16')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)  
        
    def test100_051(self):
        correct = { 'board':[5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5,
                             5, 5, 3, 4, 5, 5,
                             5, 5, 4, 3, 5, 5,
                             5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                    'status': 'ok', 
                    'integrity': 'b87b212e557d1dc1080f1c6e380bab404ae8cffa048b86e649e54c620f0d9c6a'}
        self.setLight('3')
        self.setDark('4')
        self.setBlank('5')
        self.setSize('6')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_052(self):
        correct = { 'board':[5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 3, 4, 5, 5, 5,
                             5, 5, 5, 4, 3, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5,
                             5, 5, 5, 5, 5, 5, 5, 5], 
                    'tokens': {'light': 3, 'dark': 4, 'blank': 5}, 
                    'status': 'ok', 
                    'integrity': '306a2474c8f8b41c9e31af0fe360f9fcaf3531b3b4a1c3624acd8fbc2530b02e'}
        self.setLight('3')
        self.setDark('4')
        self.setBlank('5')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
    
    def test100_060(self):
        correct = { 'board':[0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 1, 2, 0, 0, 0,
                             0, 0, 0, 2, 1, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0], 
                    'tokens': {'light': 1, 'dark': 2, 'blank': 0}, 
                    'status': 'ok', 
                    'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'}
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_070(self):
        correct = { 'board':[0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 1, 2, 0, 0, 0,
                             0, 0, 0, 2, 1, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0], 
                    'tokens': {'light': 1, 'dark': 2, 'blank': 0}, 
                    'status': 'ok', 
                    'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'}
        self.setExtra('1234')
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
        
    def test100_903(self):
        correct = {'status': self.error1}
        self.setLight(None)
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_910(self):
        correct = {'status': self.error2}
        self.setDark('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_911(self):
        correct = {'status': self.error2}
        self.setDark('-1')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_912(self):
        correct = {'status': self.error1}
        self.setDark('d')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_913(self):
        correct = {'status': self.error1}
        self.setDark(None)
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
    
    def test100_920(self):
        correct = {'status': self.error2}
        self.setBlank('10')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_921(self):
        correct = {'status': self.error2}
        self.setBlank('-1')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_922(self):
        correct = {'status': self.error1}
        self.setBlank('b')
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
        
    def test100_923(self):
        correct = {'status': self.error1}
        self.setBlank(None)
        result = create._create(self.inputDictionary)
        self.assertEqual(correct, result)
    
    