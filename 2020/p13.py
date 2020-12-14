#!/usr/bin/env python

from utils import *
from math import *

def part_one(inputs):
    ts = int(inputs[0])
    buses = [int(x) for x in inputs[1].split(',') if x != 'x']
    small = min([((((ts//x)+1)*x)-ts,x) for x in buses], key=lambda x: x[0])
    return small[0]*small[1]

def check_buses(i, buses):
    for bus in buses:
        if (i+bus[0])%bus[1] != 0:
            return False
    return True

def part_two(inputs, start):
    buses = sorted([(i,int(x)) for i,x in enumerate(inputs[1].split(',')) if x != 'x'], key=lambda x: -x[1])
    i = start // buses[0][1]
    while True:
        if check_buses((buses[0][1]*i)-buses[0][0], buses):
            return (buses[0][1]*i)-buses[0][0]
        i+=1
    
    # This brute force method never actually completed. Ended up putting 
    # x+41=a*557,x+72=b*419,x+0=c*41,x+35=d*37,x+43=e*29,x+64=f*23,x+91=g*19,x+58=h*17,x+54=i*13
    # into wolfram alpha to see that it generates the function
    # x = 598411311431841 + 991577143594063 n
    # so for n = 0, x = 598411311431841
    # 500 trillion / ~500 (the biggest bus value) is still 5 trillion, which is still a week of 
    # processing assuming I test one index per nanosecond (yeah right) 
    # Part Two big time fail, but hey, we got the answer.  More googling of "math multiple sequence intersection"
    # leads to reddit.com/r/askmath/comments/23macl/given_2_different_arithmetic_progressions_is/
    # where they start talking about the "Chinese Remainder Theorem" so maybe that would work

s = start_time()
# Part One 
print(part_one(aocin('inputs/13.1')))
print(part_one(aocin('inputs/13')))
end_time(s)

s = start_time()
# Part One 
print(part_two(aocin('inputs/13.1'), 1000000))
# print(part_two(aocin('inputs/13'), 100000000000000)) # never completes!  
end_time(s)
