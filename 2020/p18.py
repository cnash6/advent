#!/usr/bin/env python

from utils import *

def do_math(equation): # garbage
    ans,op = 0,None
    while equation:
        n = equation.split(' ',1)[0]
        if n[0] == '(':     
            parens,i = 1,1
            while parens > 0:
                if equation[i] == '(':
                    parens+=1
                elif equation[i] == ')':
                    parens-=1
                i+=1
            sub = equation[0:i+1].strip()
            math = str(do_math(sub[1:-1].strip()))
            equation = math + ' ' + equation[len(sub):].strip()
        else:
            if n.isdigit():
                ans = eval(f'{ans} {op} {n}') if op else n
            else:
                op = n
            equation = equation[len(n)+1:]
    return ans

def do_advanced_math(equation):
    equation = [x for x in equation if x != ' ']
    while len(equation) > 1:
        if '(' in equation:
            i = equation.index('(')
            parens,j = 1,i+1
            while parens > 0:
                if equation[j] == '(':
                    parens+=1
                elif equation[j] == ')':
                    parens-=1
                j+=1
            equation = equation[:i] + [do_advanced_math(equation[i+1:j-1])] + equation[j:]
        elif '+' in equation:
            i = equation.index('+')
            equation = equation[:i-1] + [int(equation[i-1]) + int(equation[i+1])] + equation[i+2:]
        elif '*' in equation:
            i = equation.index('*')
            equation = equation[:i-1] + [int(equation[i-1]) * int(equation[i+1])] + equation[i+2:]
    return equation[0]
    
def part_one(inputs):
    return sum(do_math(x) for x in inputs)

def part_two(inputs):
    return sum(do_advanced_math(x) for x in inputs)

s = start_time()
print(part_one(aocin('inputs/18'))) 
end_time(s)

s = start_time()
print(part_two(aocin('inputs/18'))) 
end_time(s)
