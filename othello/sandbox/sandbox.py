'''
    Created on Mar 12, 2020
    @author: Kun Ding
'''


import hashlib



#hashlib
a = hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
print(a)

integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'

m = hashlib.sha256(b'000000000000001200002100000000000000/1/2/0/2').hexdigest()

print(m == integrity)

string = '000000000000001200002100000000000000/1/2/0/2'
m2 = hashlib.sha256(string.encode()).hexdigest()
print(m2 == integrity)

#''.join()
a = [1,2,3,4,5]
b = ''.join(str(x) for x in a)
print(b)

c = str(a)
print(c)
print(type(c))


#dictionary

a = {'a':1, 'b':2}
b = {'b':2, 'a':1}

print(a == b)
