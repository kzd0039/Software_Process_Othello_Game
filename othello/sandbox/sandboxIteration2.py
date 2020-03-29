"""
    Created to test code segment
    Baselined: Mar 28, 2020
    @Author: Kun Ding
"""
import collections
import math

#methods to validate integrity
integrity1 = [0,0,0,0,0,0,
              0,0,0,0,0,0,
              0,0,1,2,0,0,
              0,0,2,1,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,0]

count1 = collections.Counter(integrity1)
print(count1,count1[0],count1[3])

integrity2 = [0,0,0,0,0,0,
              0,0,0,0,0,0,
              0,0,1,2,0,0,
              0,0,2,1,0,0,
              0,0,0,0,0,0,
              0,0,0,0,0,'1bcddd']
count2 = collections.Counter(integrity2)
print(count2)

a = 36
root = int(math.sqrt(a))
print(root)