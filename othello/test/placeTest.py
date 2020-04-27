'''
    Created to test place
    Baselined: April 25, 2020
    Modified: April 26, 2020
    Modified: April 27, 2020
    @Author: Kun Ding
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
        self.error10 = 'error: invalid location'
        self.error11 = 'error: missing integrity'
        self.error12 = 'error: invalid integrity'
        self.error13 = 'error: incorrect integrity'
        self.error14 = 'error: incorrect location'
        self.error15 = 'error: location out-of-bound'
        self.error16 = 'error: location occupied'
      
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
        
       
    
    #happy path  
    def test300_001(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'board': '[0,0,0,0,0,0,0,0,2,0,0,0,0,0,2,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]', 
                   'integrity': 'eaf8d3a826f7f59529add5f9eb60310ab9e936b3556e64a35ac67fef8370094a', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
       
       
    def test300_002(self):
        self.setOperation('place')
        self.setBlank('0')
        self.setLocation('3:2')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'board': '[0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]', 
                   'integrity': 'a77317b8b0f45b47570631cfaec637f8be98fb0b2efcc2a50e05edaf7aa12332', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
        
    def test300_003(self):  
        self.setOperation('place')
        self.setLight('9')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('4:5')
        board = '[0,0,0,0,0,0,0,0,2,9,0,0,0,0,9,9,0,0,0,9,2,9,0,0,0,2,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '4e0d3cd221a2623ae1876d772856e3c57e5da3905717e91eb29229f0bfc52af2'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'board': '[0,0,0,0,0,0,0,0,2,9,0,0,0,0,9,2,0,0,0,9,2,2,2,0,0,2,0,0,0,0,0,0,0,0,0,0]', 
                   'integrity': '3fb195ee12f9815782f334fd53e78b4ab5c00f830d1f0f54839fa82d09085165', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
    
    def test300_004(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('9')
        self.setBlank('1')
        self.setLocation('4:5')
        board = '[1,1,1,1,1,1,1,1,1,1,9,3,1,1,1,1,1,1,3,3,1,1,1,1,1,3,9,3,1,1,1,1,1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        integrity = '2ed2206afe12c5d65df665a6e4f6bf7ddd551abaffbacdd73a5df032e85beade'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'board': '[1,1,1,1,1,1,1,1,1,1,9,3,1,1,1,1,1,1,3,9,1,1,1,1,1,3,9,9,9,1,1,1,1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]', 
                   'integrity': '76e13f831fd2600ef27eb4abf1dbf335d40010b25178aaf6708d6d2dbed989bb', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
    def test300_011(self):  
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('3:5')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = 'c9fd7c0049f79f33e45998064cd1fca01600dd5cdc55cb3bf33169cd07c1905a'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]', 
                   'integrity': 'f717bc92d80a8d2e16c96bcefc4d71246b7af9c4a7f671d5290e28fde4029bfd', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
    
    def test300_012(self):
        self.setOperation('place')
        self.setLight('1')
        self.setLocation('5:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = 'c9fd7c0049f79f33e45998064cd1fca01600dd5cdc55cb3bf33169cd07c1905a'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]', 
                   'integrity': '3dc3c01b2aec20e3abf3c8e43d97bc4166cc9a8a7151cc5587db03a9ff9ab77e', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
    def test300_013(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('9')
        self.setBlank('0')
        self.setLocation('8:10')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '94cdef5db1b841b614c703db1c1f97146ae5fe1b4e82292a0d343ee652247618'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,9,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]', 
                   'integrity': '9d8ea2957f8b4e4c8e907d01f4b1bb2fb94bffe45d43592c23895ab5cb7d3d64', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
    def test300_021(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('1:1')
        board = '[0,2,2,2,2,0,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]'
        self.setBoard(board)
        integrity = 'f8db8a2cdc2f269122824f67025b35b405b6f271904a8433759b5035524decc3'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[1,2,2,2,2,0,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]', 
                   'integrity': 'e23da4f11138de543a420a3cfebd967bbf4fea360ceab05af39d9f9c63dd7506', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
        
    def test300_022(self):
        self.setOperation('place')
        self.setBlank('9')
        self.setLocation('1:8')
        board = '[9,2,2,2,2,2,2,9,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9]'
        self.setBoard(board)
        integrity = '918c9fdbd576d28edf155f8a602ea625631b3e44ed734fca0c1798259119bfa6'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[9,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9]', 
                   'integrity': '578dd5bda7781aec09fdd51d2df93582bc6c404e0a22d5735cb34408a9c40a91', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
        
        
    def test300_031(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('1:1')
        board = '[0,1,1,1,1,0,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]'
        self.setBoard(board)
        integrity = 'da3f7ca4a27610283a942fa00eb8e660ee758e4dbb97dde8b483c7725e25f1be'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[2,1,1,1,1,0,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]', 
                   'integrity': '8dd31c35e2ed54cdb355adee198d93daac5836fc702838b7c2a8aebe1d9d59c9', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
    
    def test300_032(self):
        self.setOperation('place')
        self.setLocation('8:8')
        board = '[0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]'
        self.setBoard(board)
        integrity = '8f1c9c06ea39aa9ae0c748795c33b9bd51dc66d4e8944a27c070f728543551c4'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2]', 
                   'integrity': '805aba61857118a247a841aec84e3ae5c9baac8fc69881eb06b2dfe0c4568ce1', 
                   'status': 'ok'}
        self.assertEqual(correct, result)
    
    def test300_041(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('8:8')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]'
        self.setBoard(board)
        integrity = 'bc2cef741e4537e4b78559f9ed8d4848216ebe3e56676ff3bf66dfc03db1a857'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2]', 
                   'integrity': '1b4ff0d66dbca4dfa6e4585ea88452851105a8f4f5d0eb43efbc56baab8d87dc', 
                   'status': 'end:59/5'}
        self.assertEqual(correct, result)
        
        
    def test300_042(self):   
        self.setOperation('place')
        self.setLight('3')
        self.setDark('4')
        self.setBlank('0')
        self.setLocation('8:8')
        board = '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0]'
        self.setBoard(board)
        integrity = '3f36680614c2b53ebaa65f5e4b7ab31fb31fea2f10b92a0cdb39953a2d5ed36e'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4]', 
                   'integrity': '8402bbbd494d120f77786124bafe5373c36177b18505afa767b0be81311200f6', 
                   'status': 'end:59/5'}
        self.assertEqual(correct, result)
        
    def test300_043(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('4')
        self.setBlank('5')
        self.setLocation('10:10')
        board = '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5]'
        self.setBoard(board)
        integrity = 'cc988c1e4c1a94995d51cb0cd1aab27ba3861afa9088049cb6ddf677514980e1'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4]', 
                   'integrity': '5b903926f9fcf90eb229fd30992436de4a4895806bf5b6f13f24921cbf810a01', 
                   'status': 'end:93/7'}
        self.assertEqual(correct, result)
    
    def test300_051(self):
        self.setOperation('place')
        self.setLight('2')
        self.setDark('1')
        self.setBlank('0')
        self.setLocation('8:8')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]'
        self.setBoard(board)
        integrity = 'd3c64bc0b9471cf272072140ee7f4a26ca31aed3feb789308c173b831913c495'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2]', 
                   'integrity': '1bcb08a73744b1bd078948fe7c29d249d49034ca92dce421d06d73cdcdeb936a', 
                   'status': 'end:5/59'}
        self.assertEqual(correct, result)
        
    def test300_052(self): 
        self.setOperation('place')
        self.setLight('4')
        self.setDark('3')
        self.setBlank('0')
        self.setLocation('8:8')
        board = '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0]'
        self.setBoard(board)
        integrity = '0a9b1c454dc120015fcabbb3d988b34635f5faf498be629d837c08d5c8b77998'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)
        correct = {'board': '[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4]', 
                   'integrity': '6c846bc658e900ca4302e3d8ed1255b24d95995a1e10d7ace857ed0f33faa2ec', 
                   'status': 'end:5/59'}
        self.assertEqual(correct, result)
        
         
        #sad path  
    def test300_900LightNonInteger(self):
        self.setOperation('place')
        self.setLight('X')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,X,2,0,0,0,0,2,X,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error1}
        self.assertEqual(result, correct)
        
         
    def test300_901LightNonInteger(self):
        self.setOperation('place')
        self.setLight('1.5')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1.5,2,0,0,0,0,2,1.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
       
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
          
          
    def test300_902LightOutOfUpperBound(self):
        self.setOperation('place')
        self.setLight('10')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,2,0,0,0,0,2,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
          
    def test300_903LightOutOfLowerBound(self):
        self.setOperation('place')
        self.setLight('-1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,2,0,0,0,0,2,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
        
    def test300_904LightNull(self):
        self.setOperation('place')
        self.setLight('')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
          
    def test300_910DarkNonInteger(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('X')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,X,0,0,0,0,X,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)

         
    def test300_911DarkNonInteger(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('1.5')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1.5,0,0,0,0,1.5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)

          
    def test300_912DarkOutOfUpperBound(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('10')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,10,0,0,0,0,10,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
        

          
    def test300_913DarkOutOfLowerBound(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('-1')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
        
   
    def test300_914DarkNull(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
   
          
    def test300_920BlankNonInteger(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('X')
        self.setLocation('2:3')
        board = '[X,X,X,X,X,X,X,X,X,X,X,X,X,X,1,2,X,X,X,X,2,1,X,X,X,X,X,X,X,X,X,X,X,X,X,X]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)

          
    def test300_921BlankNonInteger(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('1.5')
        board = '[1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1,2,1.5,1.5,1.5,1.5,2,1,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity) 
        correct = {'status': self.error1}
        result = place._place(self.inputDictionary) 
        self.assertEqual(result, correct)
          
    def test300_922BlankOutOfUpperBound(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('10')
        self.setLocation('2:3')
        board = '[10,10,10,10,10,10,10,10,10,10,10,10,10,10,1,2,10,10,10,10,2,1,10,10,10,10,10,10,10,10,10,10,10,10,10,10]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)

           
    def test300_923BlankOutOfLowerBound(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('-1')
        self.setLocation('2:3')
        board = '[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,2,-1,-1,-1,-1,2,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)      
        correct = {'status': self.error2}
        result = place._place(self.inputDictionary)
        self.assertEqual(result, correct)
    
    def test300_924BlankNull(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error1}
        self.assertEqual(result, correct)
        
      
    def test300_930LightEqualsBlank(self):
        self.setOperation('place')
        self.setLight('0')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error3}
        self.assertEqual(result, correct)


         
    def test300_931LightEqualsDark(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('1')
        self.setBlank('0')
        self.setLocation('2:3')
        board = '[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
        self.setBoard(board)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error3}
        self.assertEqual(result, correct)
        
        
      
    def test300_940BoardMissing(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error4}
        self.assertEqual(result, correct)
           
    def test300_941BoardNull(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('0')
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setBoard(None) 
        self.setIntegrity(integrity)
        result = place._place(self.inputDictionary)       
        correct = {'status': self.error4}
        self.assertEqual(result, correct)
  
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
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error5}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   
  
    def test300_943BoardSizeOutOfBound(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,2,3,1,1,1,1,1,1]'
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error6}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   
  
    def test300_944BoardSizeOdd(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error7}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)   
  
    def test300_945BoardWithNonLightDarkBlankTokens(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,4,1,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'       
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
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
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error9}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 
   
    def test300_951LocationNull(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        self.setLocation(None)
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error9}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 
  
    def test300_952LocationInvalid(self):
        self.setOperation('place')
        self.setLight('3')
        self.setDark('2')
        self.setBlank('1')
        board = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,2,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]'
        self.setBoard(board)
        self.setLocation('x:2')
        integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
        self.setIntegrity(integrity)
        correct = {'status': self.error10}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result) 
        
    def test300_953LocationOutOfBound(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('1:10')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'        
        self.setIntegrity(integrity)
        correct = {'status': self.error15}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
          
    def test300_954LocationOccupied(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('3:3')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'        
        self.setIntegrity(integrity)
        correct = {'status': self.error16}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
  
    def test300_955LocationIncorrect(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('1:3')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'        
        self.setIntegrity(integrity)
        correct = {'status': self.error14}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
  
    def test300_960IntegrityMissing(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('2:3')
        correct = {'status': self.error11}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
      
    def test300_961IntegrityNull(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setIntegrity(None)
        self.setLocation('2:3')
        correct = {'status': self.error11}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
#          
    def test300_962IntegrityInvalidShort(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a0'
        self.setIntegrity(integrity)
        correct = {'status': self.error12}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
          
    def test300_963IntegrityInvalidLong(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a000'
        self.setIntegrity(integrity)
        correct = {'status': self.error12}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  
  
    def test300_964IntegrityIncorrect(self):
        self.setOperation('place')
        self.setLight('1')
        self.setDark('2')
        self.setBlank('3')
        board='[3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,3,3,3,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3]'
        self.setBoard(board)
        self.setLocation('2:3')
        integrity = 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465b'     
        self.setIntegrity(integrity)
        correct = {'status': self.error13}
        result = place._place(self.inputDictionary)
        self.assertEqual(correct, result)  







