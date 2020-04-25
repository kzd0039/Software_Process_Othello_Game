'''
    Created to test place
    Baselined: April 25, 2020
'''

import unittest
import othello.place as place

class statusTest(unittest.TestCase):
    def setUp(self):
        self.inputDictionary = {}
        self.error1 = 'error: light/blank/dark non-integer'
        self.error2 = 'error: light/blank/dark out of bounds'
        self.error3 = 'error: light/blank/dark not unique'
        self.error4 = 'error: missing board'
        self.error5 = 'error: non-square board'
        self.error6 = 'error: board size out of bounds'
        self.error7 = 'error: odd board'
        self.error8 = 'error: board with non-light/dark/blank tokens'
        self.error9 = 'error: missing location'
#         self.error8 = 'error: missing integrity'
#         self.error9 = 'error: invalid integrity'

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
        self.setOperation('place')
        self.setLight('X')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_901LightNonInteger(self):
        self.setOperation('place')
        self.setLight('1.5')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_902LightOutOfUpperBound(self):
        self.setOperation('place')
        self.setLight('10')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct) 
        
    def test300_903LightOutOfLowerBound(self):
        self.setOperation('place')
        self.setLight('-1')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct) 
        
    def test300_910DarkNonInteger(self):
        self.setOperation('place')
        self.setDark('X')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_911DarkNonInteger(self):
        self.setOperation('place')
        self.setDark('1.5')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_912DarkOutOfUpperBound(self):
        self.setOperation('place')
        self.setDark('10')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct) 
        
    def test300_913DarkOutOfLowerBound(self):
        self.setOperation('place')
        self.setDark('-1')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)     
        
    def test300_920BlankNonInteger(self):
        self.setOperation('place')
        self.setBlank('X')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_921BlankNonInteger(self):
        self.setOperation('place')
        self.setBlank('1.5')
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)
        
    def test300_922BlankOutOfUpperBound(self):
        self.setOperation('place')
        self.setBlank('10')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct) 
        
    def test300_923BlankOutOfLowerBound(self):
        self.setOperation('place')
        self.setBlank('-1')
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)       
    
    def test300_930LightEqualsBlank(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('1')
        correct = {'status': self.error3}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)  
        
    def test300_931LightEqualsDark(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('1')
        self.setBlank('0')
        correct = {'status': self.error3}
        result = place._place(self.inputDictionary)
        
        self.assertEqual(result, correct)  
    
    def test300_940BoardMissing(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        integrity = '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'
        self.setIntegrity(integrity)
     
        correct = {'status': self.error4}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   
         
    def test300_941BoardEqualsNone(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        self.setBoard(None)
      
        correct = {'status': self.error4}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   

    def test300_942BoardNonSquare(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,\
                 1,1,1,1,1,1,\
                 1,1,3,2,1,1,\
                 1,1,2,3,1,1,\
                 1,1,1,1,1,1,\
                 1,1,1,1,1]'
        self.setBoard(board)
      
        correct = {'status': self.error5}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   

    def test300_943BoardSizeOutOfBound(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1\
                 1,1,1,1,1,\
                 1,1,3,2,1,\
                 1,1,2,3,1,\
                 1,1,1,1,1,]'
           
        self.setBoard(board)
      
        correct = {'status': self.error6}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   

    def test300_944BoardSizeOdd(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1,\
                 1,1,1,1,1,1,1]'
           
        self.setBoard(board)
      
        correct = {'status': self.error7}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   

    def test300_945BoardWithNonLightDarkBlankTokens(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,\
                 1,1,1,1,1,1,\
                 1,1,3,4,1,1,\
                 1,1,4,3,1,1,\
                 1,1,1,1,1,1,\
                 1,1,1,1,1,1]'
           
        self.setBoard(board)
      
        correct = {'status': self.error8}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 

    def test300_950LocationMissing(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        correct = {'status': self.error9}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 

    def test300_951LocationEqualsNone(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        self.setLocation(None)
        correct = {'status': self.error9}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 














