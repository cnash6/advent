# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29  
# 40  19   6   1   2  11  28  53
# 41  20   7   8   9  10  27  52
# 42  21  22  23  24  25  26  51
# 43  44  45  46  47  48  49  50

# Part One

x = 1
y = 0

e = 1
n = 2
N = 289326

def is_target(t):
  if n == N:
    print(str(n) + ": " + str(x) + "," + str(y))
    print(abs(x) + abs(y))

while n < N:
  for i in range(2*e - 1):
    y+=1
    n+=1
    is_target(n)
  for i in range(2*e):
    x-=1
    n+=1
    is_target(n)
  for i in range(2*e):
    y-=1
    n+=1
    is_target(n)
  for i in range(2*e + 1):
    x+=1
    n+=1
    is_target(n)
  e+=1

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

# Part Two

def add_em(steps, x, y):
  asum = 0
  if str(x+1) + "," + str(y) in steps:
    asum+=steps[str(x+1) + "," + str(y)]
  if str(x+1) + "," + str(y+1) in steps:
    asum+=steps[str(x+1) + "," + str(y+1)]
  if str(x) + "," + str(y+1) in steps:
    asum+=steps[str(x) + "," + str(y+1)]
  if str(x-1) + "," + str(y+1) in steps:
    asum+=steps[str(x-1) + "," + str(y+1)]
  if str(x-1) + "," + str(y) in steps:
    asum+=steps[str(x-1) + "," + str(y)]
  if str(x-1) + "," + str(y-1) in steps:
    asum+=steps[str(x-1) + "," + str(y-1)]
  if str(x) + "," + str(y-1) in steps:
    asum+=steps[str(x) + "," + str(y-1)]
  if str(x+1) + "," + str(y-1) in steps:
    asum+=steps[str(x+1) + "," + str(y-1)]
  steps[str(x) + "," + str(y)] = asum
  return asum


def do_it():

  x = 1
  y = 0

  e = 1
  last = 0
  N = 289326

  steps = {}
  steps[str(0) + "," + str(0)] = 1

  while last < N:
    for i in range(2*e - 1):
      last = add_em(steps, x, y)
      if last > N:
        return "found: " + str(last)
      y+=1
    for i in range(2*e):
      last = add_em(steps, x, y)
      if last > N:
        return "found: " + str(last)
      x-=1
    for i in range(2*e):
      last = add_em(steps, x, y)
      if last > N:
        return "found: " + str(last)
      y-=1
    for i in range(2*e + 1):
      last = add_em(steps, x, y)
      if last > N:
        return "found: " + str(last)
      x+=1
    e+=1

print(do_it())

