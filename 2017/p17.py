#!/usr/bin/env python3
from collections import deque
from utils import check_progress

if __name__ == '__main__':
  puzzle_in = 382

  lock = deque([0])
  N = 50000000
  for n in range(1,N+1):
    check_progress(n-1, N)
    lock.rotate(-1 * (puzzle_in+1) % len(lock))
    lock.appendleft(n)

  found = list(lock)
  print(found[found.index(0)+1])