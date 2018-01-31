#!/usr/bin/env python3
from utils import check_progress

def turn_left(d):
  if d == 'n':
    return 'e'
  if d == 'e':
    return 's'
  if d == 's':
    return 'w'
  if d == 'w':
    return 'n'

def turn_right(d):
  if d == 'n':
    return 'w'
  if d == 'w':
    return 's'
  if d == 's':
    return 'e'
  if d == 'e':
    return 'n'  

if __name__ == '__main__':
  f = open('assets/22.txt', 'r')
  starting_nodes = [[y for y in x.strip()] for x in f]
  # print(starting_nodes)

  N = 10000000

  # Build graph with origin in the middle
  nodes = {}
  off_y = len(starting_nodes)//2
  off_x = -(len(starting_nodes[0])//2)
  for y in range(len(starting_nodes)):
    for x in range(len(starting_nodes[y])):
      nodes[(off_x+x,off_y-y)] = starting_nodes[y][x]

  d = 'n'
  x,y,c = 0,0,0
  for n in range(N):
    check_progress(n-1, N)
    # print(x,y)
    # print(d)
    if (x,y) in nodes and nodes[(x,y)] == '#':
      # print("# => F")
      # print("turn right")
      d = turn_right(d)
      nodes[(x,y)] = 'F'
    elif (x,y) in nodes and nodes[(x,y)] == 'W':
      # print("W => #")
      # print("go straight")
      c+=1
      nodes[(x,y)] = '#'
    elif (x,y) in nodes and nodes[(x,y)] == 'F':
      # print("F => .")
      # print("turn around")
      d = turn_right(d)
      d = turn_right(d)
      nodes[(x,y)] = '.'
    else:
      # print(". => W")
      # print("turn left")
      d = turn_left(d)
      nodes[(x,y)] = 'W'

    if d == 'n':
      y+=1
    if d == 's':
      y-=1
    if d == 'e':
      x-=1
    if d == 'w':
      x+=1

    # print(x,y)
    # print(d)
    # input("Press Enter to continue...")
print()
print(c)

