#!/usr/bin/env python3
from collections import deque

def spin(programs, distance):
  items = deque(programs)
  items.rotate(distance)
  return list(items)

def exchange(programs, a, b):
  programs[a], programs[b] = programs[b], programs[a]
  return programs

def partner(programs, a, b):
  a_i, b_i = programs.index(a), programs.index(b)
  programs[a_i], programs[b_i] = programs[b_i], programs[a_i]
  return programs

def dance(programs, moves):
  for move in moves:
    if move[0] is 's':
      programs = spin(programs, int(move[1:]))
    if move[0] is 'x':
      a,b = move[1:].split('/')
      programs = exchange(programs, int(a), int(b))
    if move[0] is 'p':
      a,b = move[1:].split('/')
      programs = partner(programs, a, b)
  return programs

def check_progress(i, n):
  if i % (n//100) == 0:
    print("..." + str(i // (n//100)) + "%", end="\r")

if __name__ == '__main__':
  f = open('assets/16.txt', 'r')
  moves = [x.strip() for x in f.read().split(',')]
  # moves = ['s1', 'x3/4', 'pe/b']

  programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
  # programs = ['a','b','c','d','e'] # Test

  N = 1000000000
  n = 0
  perms = [programs]
  for i in range(N):
    check_progress(i, N)
    programs = dance(programs, moves)
    if programs in perms:
      n = i
      break
    else:
      perms.append(programs)

  found = perms[N % len(perms)]


  print("".join(found))