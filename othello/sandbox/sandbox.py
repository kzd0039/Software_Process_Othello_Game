'''
    Created on Mar 12, 2020
    @author: Kun Ding
'''


import hashlib

a = hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
print(a)

integrity = '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'

m = hashlib.sha256(b"000000000000001200002100000000000000/1/2/0/2").hexdigest()

print(m == integrity)

