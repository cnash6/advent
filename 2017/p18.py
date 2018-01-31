# f = open('assets/18.txt', 'r')
# instructions = [x.strip().split(' ') for x in f.readlines()]

# def is_digit(n):
#     try:
#         int(n)
#         return True
#     except ValueError:
#         return  False

# def sound(registers, x):
#   # print("sound " + str(x))
#   if is_digit(x):
#     return x
#   else:
#     return registers[x]

# def set_r(registers, x, y):
#   # print("set " + str(x) + ":" + str(y))
#   if is_digit(y):
#     registers[x] = int(y)
#   else:
#     registers[x] = registers[y]

# def add_r(registers, x, y):
#   # print("add " + str(x) + ":" + str(y))
#   if is_digit(y):
#     registers[x] = registers[x] + int(y)
#   else:
#     registers[x] = registers[x] + registers[y]

# def mult_r(registers, x, y):
#   # print("mult " + str(x) + ":" + str(y))
#   if is_digit(y):
#     registers[x] = registers[x] * int(y)
#   else:
#     registers[x] = registers[x] * registers[y]

# def mod_r(registers, x, y):
#   # print("mod " + str(x) + ":" + str(y))
#   if is_digit(y):
#     registers[x] = registers[x] % int(y)
#   else:
#     registers[x] = registers[x] % registers[y]

# def jump(i, registers, x, y):
#   # print("jump " + str(x) + ":" + str(y))
#   if is_digit(y):
#     return i + int(y) if registers[x] > 0 else i+1
#   else:
#     return i + registers[y] if registers[x] > 0 else i+1
  

# def execute(instructions, state):
#   # print(state['registers'])
#   instruction = instructions[state['i']]
#   registers = state['registers']

#   if instruction[1] not in registers:
#     registers[instruction[1]] = 0
#   if len(instruction) > 2 and not is_digit(instruction[2]) and instruction[2] not in registers:
#     registers[instruction[2]] = 0

#   if instruction[0] == 'rcv':
#     print("rcv " + instruction[1] )
#     if len(state['stack']) > 0:
#       val = state['stack'].pop(0)
#       registers[instruction[1]] = val if is_digit(val) else registers[val]
#       if len(state['stack']) == 0:
#         print("blocked now")
#         state['blocked'] = True
#     else:
#       print("None to receive")
#       return 'rcv'
      

#   if instruction[0] == 'set':
#     set_r(registers, instruction[1], instruction[2])
#   if instruction[0] == 'add':
#     add_r(registers, instruction[1], instruction[2])
#   if instruction[0] == 'mul':
#     mult_r(registers, instruction[1], instruction[2])
#   if instruction[0] == 'mod':
#     mod_r(registers, instruction[1], instruction[2])

#   if instruction[0] == 'jgz':
#     state['i'] = jump(state['i'], registers, instruction[1], instruction[2])
#   else:
#     state['i'] = state['i']+1

#   # print(state['registers'])

#   if instruction[0] == 'snd':
#     print("send" + instruction[1])
#     return sound(registers, instruction[1])
#   return None
# https://github.com/grvn/aoc2017/blob/master/18/d18-2.py

# if __name__ == '__main__':
#   registers = {}

#   a_state = {
#     'registers': {},
#     'stack': [],
#     'i': 0,
#     'blocked': False

#   }
#   b_state = {
#     'registers': {},
#     'stack': [],
#     'i': 0,
#     'blocked': False
#   }

#   running = True
#   run_a = True
#   c = 0

#   while running:
#     if run_a:
#       # print("run_a")
#       msg = execute(instructions, a_state)
#       if msg == 'rcv':
#         run_a = False
#       elif msg != None:
#         b_state['stack'].append(msg)
#         b_state['blocked'] = False
#         c+=1
      
#     else:
#       # print("run_b")
#       msg = execute(instructions, b_state)
#       if msg == 'rcv':
#         run_a = True
#       elif msg != None:
#         a_state['stack'].append(msg)
#         a_state['blocked'] = False

#     if a_state['blocked'] and b_state['blocked']:
#       print("Done")
#       print(c)
#       break

#     # input("Press Enter to continue...")
#!/usr/bin/env python3

from sys import argv
from threading import Thread
from queue import Queue
from collections import defaultdict

filename=argv[1]
reg0=defaultdict(lambda:0)
reg1=defaultdict(lambda:0)
reg1['p']=1 
pos0=0
pos1=0
to0=Queue()
to1=Queue()

with open(filename) as f:
    input = f.readlines()
    input = [line.split() for line in input]

def extract(reg, val):
    try:
        int(val)
        return int(val)
    except ValueError:
        return reg[val]
    
def worker(id,reg,pos,to,fro):
    co=0
    while True:
        ins = input[pos]
        if ins[1] not in reg:
            reg[ins[1]]=0
        if ins[0]=='set':
            reg[ins[1]]=extract(reg,ins[2])
        elif ins[0]=='add':
            reg[ins[1]]+=extract(reg,ins[2])
        elif ins[0]=='mul':
            reg[ins[1]]*=extract(reg,ins[2])
        elif ins[0]=='mod':
            reg[ins[1]]%=extract(reg,ins[2])
        elif ins[0]=='snd':
            to.put(extract(reg,ins[1]))
            co+=1
        elif ins[0]=='rcv':
            try:
                reg[ins[1]]=fro.get(True,1)
            except:
                print("Thread",id,":",co)
                return
        elif ins[0]=='jgz':
            if extract(reg,ins[1]) > 0:
                pos+=extract(reg,ins[2])
                continue
        pos+=1


t0=Thread(target=worker, args=(0,reg0,pos0,to0,to1))
t1=Thread(target=worker, args=(1,reg1,pos1,to1,to0))
t0.start()
t1.start()
t0.join()
t1.join()




