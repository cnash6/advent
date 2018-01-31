# !/usr/bin/env python3
from collections import defaultdict

def extract(reg, val):
  try:
    int(val)
    return int(val)
  except ValueError:
    return reg[val]

if __name__ == '__main__':
  f = open('assets/23.txt', 'r')
  instructions = [x.strip().split(" ") for x in f]

  c = 0
  i = 0
  reg = defaultdict(int)
  reg['a'] = 1
  print(reg)

  while 0 <= i < len(instructions)-1:
    ins = instructions[i]

    if ins[0] == "set":
      reg[ins[1]] = extract(reg,ins[2])
    elif ins[0] == "sub":
      reg[ins[1]] -= extract(reg,ins[2])
    elif ins[0] == "mul":
      reg[ins[1]] *= extract(reg,ins[2])
      c+=1
    else: # jnz
      if extract(reg,ins[1]) != 0:
        i+=extract(reg,ins[2])
        continue
    i+=1
    if i == 30:
      print(30)
    # print(i)
    # print(reg)
    # input("Press Enter to continue...")


# print(reg['h'])
from math import sqrt; from itertools import count, islice
c = 0
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
        
for i in range(107900,124901,17):
    if not isPrime(i):
        c+=1
print("Answer:",c)