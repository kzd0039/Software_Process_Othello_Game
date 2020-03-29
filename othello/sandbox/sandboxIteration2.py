"""
    Created to test code segment
    Baselined: Mar 28, 2020
    @Author: Kun Ding
"""
import collections
import math
import hashlib

#methods to validate integrity
board1 = [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,0]

count1 = collections.Counter(board1)
print(count1,count1[0],count1[3])

board2 = [0,0,0,0,0,0,
          0,0,0,0,0,0,
          0,0,1,2,0,0,
          0,0,2,1,0,0,
          0,0,0,0,0,0,
          0,0,0,0,0,'1bcddd']
count2 = collections.Counter(board2)
print(count2)

a = 36
root = int(math.sqrt(a))
print(root)

#check which value should be chosen to be <token_to_place>, light or dark or either.

light, dark, blank = 1, 2, 0
board1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
integrity1 = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'
string_1 = ''.join(str(x) for x in board1) 
string_1_dark = string_1 + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
stirng_1_light = string_1 + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(light)

next_dark = hashlib.sha256(string_1_dark.encode()).hexdigest()
next_light = hashlib.sha256(stirng_1_light.encode()).hexdigest()

print(integrity1 == next_dark, integrity1 == next_light)



light, dark, blank = 9, 2, 0
board2 = board=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,2,0,0,0,0,2,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
integrity2 = '5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'
string_2 = ''.join(str(x) for x in board2) 
string_2_dark = string_2 + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(dark)
stirng_2_light = string_2 + '/' + str(light) + '/' +str(dark) + '/' + str(blank) + '/' + str(light)

next_dark_2 = hashlib.sha256(string_2_dark.encode()).hexdigest()
next_light_2 = hashlib.sha256(stirng_2_light.encode()).hexdigest()

print(integrity2 == next_dark_2, integrity1 == next_light_2)











