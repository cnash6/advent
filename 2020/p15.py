#!/usr/bin/env python

from utils import *

def doit(inputs, n):
    nums = [int(x) for x in inputs.split(',')]
    numd = {0: (0,0)} | {x: (i+1, 0) for i,x in enumerate(nums)}
    last = nums[-1]

    for i in range(len(nums)+1, n+1):
        say = numd[last][0]-numd[last][1] if numd[last][1] != 0 else 0
        numd[say] = (i,) + (numd[say][0],) if say in numd else (i,0)
        last = say

    return last

s = start_time()
# print(doit(aocin('inputs/15.1'), 2020)) # 436
# print(doit('1,3,2', 2020)) # 1
# print(doit('2,1,3', 2020)) # 10
# print(doit('1,2,3', 2020)) # 27
# print(doit('2,3,1', 2020)) # 78
# print(doit('3,2,1', 2020)) # 438
# print(doit('3,1,2', 2020)) # 1836
print(doit(aocin('inputs/15'), 2020))
end_time(s)

# part 2
s = start_time()
# print(doit(aocin('inputs/15.1'), 30000000)) # 175594.
# print(doit('1,3,2', 30000000)) # 2578.
# print(doit('2,1,3', 30000000)) # 3544142.
# print(doit('1,2,3', 30000000)) # 261214.
# print(doit('2,3,1', 30000000)) # 6895259.
# print(doit('3,2,1', 30000000)) # 18.
# print(doit('3,1,2', 30000000)) # 362.
print(doit(aocin('inputs/15'), 30000000))
end_time(s)


 
 
 
 
 
 